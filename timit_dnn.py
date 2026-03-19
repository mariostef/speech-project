# Train a torch DNN for Kaldi DNN-HMM model
import math
import sys
import numpy as np
import torch
import torch.nn as nn
import torch.utils.data
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from tqdm import tqdm
from dnn.torch_dataset import TorchSpeechDataset
from dnn.torch_dnn import TorchDNN

DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# CONFIGURATION #
NUM_LAYERS = 2
HIDDEN_DIM = 256
USE_BATCH_NORM = True
DROPOUT_P = .2
EPOCHS = 50
PATIENCE = 3

if len(sys.argv) < 2:
    print("USAGE: python timit_dnn.py <PATH/TO/CHECKPOINT_TO_SAVE.pt>")

BEST_CHECKPOINT = sys.argv[1]

# FIXME: You may need to change these paths
TRAIN_ALIGNMENT_DIR = "exp/tri1_ali_train"
DEV_ALIGNMENT_DIR = "exp/tri1_ali_dev"
TEST_ALIGNMENT_DIR = "exp/tri1_ali_test"


def train(model, criterion, optimizer, train_loader, dev_loader, epochs=50, patience=3):
    best_val_loss = float('inf')
    patience_counter = 0

    for epoch in range(epochs):
        # Training
        model.train()
        train_loss = 0
        all_preds, all_labels = [], []
        for feats, labels in tqdm(train_loader, desc=f"Epoch {epoch+1}/{epochs} [Train]"):
            feats, labels = feats.to(DEVICE), labels.to(DEVICE)
            optimizer.zero_grad()
            output = model(feats)
            loss = criterion(output, labels)
            loss.backward()
            optimizer.step()
            train_loss += loss.item()
            preds = output.argmax(dim=1).cpu().numpy()
            all_preds.extend(preds)
            all_labels.extend(labels.cpu().numpy())
        train_acc = accuracy_score(all_labels, all_preds)

        # Validation
        model.eval()
        val_loss = 0
        all_preds, all_labels = [], []
        with torch.no_grad():
            for feats, labels in dev_loader:
                feats, labels = feats.to(DEVICE), labels.to(DEVICE)
                output = model(feats)
                loss = criterion(output, labels)
                val_loss += loss.item()
                preds = output.argmax(dim=1).cpu().numpy()
                all_preds.extend(preds)
                all_labels.extend(labels.cpu().numpy())
        val_acc = accuracy_score(all_labels, all_preds)

        print(f"Epoch {epoch+1}: Train Loss={train_loss/len(train_loader):.4f}, Acc={train_acc:.4f} | Val Loss={val_loss/len(dev_loader):.4f}, Acc={val_acc:.4f}")

        if val_loss < best_val_loss:
            best_val_loss = val_loss
            patience_counter = 0
            torch.save(model, BEST_CHECKPOINT)
            print(f"  -> Saved best model to {BEST_CHECKPOINT}")
        else:
            patience_counter += 1
            if patience_counter >= patience:
                print(f"Early stopping at epoch {epoch+1}")
                break


trainset = TorchSpeechDataset('./', TRAIN_ALIGNMENT_DIR, 'train')
validset = TorchSpeechDataset('./', DEV_ALIGNMENT_DIR, 'dev')
testset  = TorchSpeechDataset('./', TEST_ALIGNMENT_DIR, 'test')

scaler = StandardScaler()
scaler.fit(trainset.feats)
trainset.feats = scaler.transform(trainset.feats)
validset.feats = scaler.transform(validset.feats)
testset.feats  = scaler.transform(testset.feats)

feature_dim = trainset.feats.shape[1]
n_classes = int(trainset.labels.max() - trainset.labels.min() + 1)

dnn = TorchDNN(
    feature_dim,
    n_classes,
    num_layers=NUM_LAYERS,
    batch_norm=USE_BATCH_NORM,
    hidden_dim=HIDDEN_DIM,
    dropout_p=DROPOUT_P
)
dnn.to(DEVICE)

train_loader = torch.utils.data.DataLoader(trainset, batch_size=128, shuffle=True)
dev_loader   = torch.utils.data.DataLoader(validset, batch_size=128, shuffle=False)

optimizer = torch.optim.Adam(dnn.parameters(), lr=1e-3)
criterion = nn.CrossEntropyLoss()

train(dnn, criterion, optimizer, train_loader, dev_loader, epochs=EPOCHS, patience=PATIENCE)
