import math
import os
import sys
import kaldi_io
import numpy as np
import torch
import torch.nn as nn
import torch.utils.data
from sklearn.preprocessing import StandardScaler
from tqdm import tqdm
from dnn.torch_dataset import TorchSpeechDataset
from dnn.torch_dnn import TorchDNN

if len(sys.argv) < 3:
    print("USAGE: python extract_posteriors.py <MY_TORCHDNN_CHECKPOINT> <OUTPUT_DIR>")

CHECKPOINT_TO_LOAD = sys.argv[1]
OUT_DIR = sys.argv[2]

if not os.path.exists(OUT_DIR):
    os.makedirs(OUT_DIR)
OUTPUT_ARK_FILE = os.path.join(OUT_DIR, "posteriors.ark")

DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

TRAIN_ALIGNMENT_DIR = "exp/tri1_ali_train"
TEST_ALIGNMENT_DIR  = "exp/tri1_ali_test"


def extract_logits(model, test_loader):
    model.eval()
    all_logits = []
    with torch.no_grad():
        for feats, _ in tqdm(test_loader, desc="Extracting posteriors"):
            feats = feats.to(DEVICE)
            output = torch.nn.functional.log_softmax(model(feats), dim=-1)
            all_logits.append(output.cpu())
    return torch.cat(all_logits, dim=0)


trainset = TorchSpeechDataset('./', TRAIN_ALIGNMENT_DIR, 'train')
testset  = TorchSpeechDataset('./', TEST_ALIGNMENT_DIR, 'test')

scaler = StandardScaler()
scaler.fit(trainset.feats)
testset.feats = scaler.transform(testset.feats)

test_loader = torch.utils.data.DataLoader(testset, batch_size=128, shuffle=False)

dnn = torch.load(CHECKPOINT_TO_LOAD, map_location="cpu", weights_only=False).to(DEVICE)

logits = extract_logits(dnn, test_loader)

post_file = kaldi_io.open_or_fd(OUTPUT_ARK_FILE, 'wb')

start_index = 0
testset.end_indices[-1] += 1

for i, name in enumerate(testset.uttids):
    out = logits[start_index:testset.end_indices[i]].cpu().numpy()
    start_index = testset.end_indices[i]
    kaldi_io.write_mat(post_file, out, testset.uttids[i])

post_file.close()
print(f"Posteriors saved to {OUTPUT_ARK_FILE}")
