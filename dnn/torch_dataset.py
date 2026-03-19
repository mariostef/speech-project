import os
import subprocess
import numpy as np
import torch
import torch.utils.data
import kaldi_io

class TorchSpeechDataset(torch.utils.data.Dataset):
    def __init__(self, base_path, alignment_dir, split):
        feats_scp = os.path.join(base_path, 'data', split, 'feats.scp')
        cmvn_scp = os.path.join(base_path, 'data', split, 'cmvn.scp')
        utt2spk  = os.path.join(base_path, 'data', split, 'utt2spk')
        ali_dir  = os.path.join(base_path, alignment_dir)
        mdl      = os.path.join(ali_dir, 'final.mdl')

        # Read features with CMVN
        cmd = f'apply-cmvn --utt2spk=ark:{utt2spk} scp:{cmvn_scp} scp:{feats_scp} ark:-'
        proc = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        feats_dict = {k: v for k, v in kaldi_io.read_mat_ark(proc.stdout)}

        # Read alignments
        cmd = f'ali-to-pdf {mdl} "ark:gunzip -c {ali_dir}/ali.*.gz |" ark:-'
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        ali_dict = {k: v for k, v in kaldi_io.read_vec_int_ark(proc.stdout)}

        common_keys = sorted(k for k in feats_dict if k in ali_dict)

        self.uttids      = []
        self.end_indices = []
        all_feats        = []
        all_labels       = []
        idx = 0

        for key in common_keys:
            feat = feats_dict[key]
            ali  = ali_dict[key]
            n    = min(len(feat), len(ali))
            all_feats.append(feat[:n])
            all_labels.append(ali[:n])
            idx += n
            self.end_indices.append(idx)
            self.uttids.append(key)

        self.feats  = np.vstack(all_feats).astype(np.float32)
        self.labels = np.concatenate(all_labels).astype(np.int64)
        self.labels -= self.labels.min()

    def __len__(self):
        return len(self.feats)

    def __getitem__(self, idx):
        return torch.FloatTensor(self.feats[idx]), torch.tensor(self.labels[idx])
