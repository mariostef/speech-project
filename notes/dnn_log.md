# 2026-03-20 — Step 4.5: DNN-HMM με PyTorch

## What was done

- Εγκατάσταση `kaldi-io-for-python` και `PyTorch`
- Δημιουργία φακέλου `dnn/` με τα αρχεία `torch_dnn.py`, `torch_dataset.py`, `__init__.py`
- Δημιουργία `timit_dnn.py` και `extract_posteriors.py` στο root
- Εξαγωγή triphone alignments για train/dev/test
- Υπολογισμός CMVN statistics για train/dev/test
- Εκπαίδευση DNN με early stopping
- Εξαγωγή log-posteriors σε `dnn_out/posteriors.ark`
- Αποκωδικοποίηση με `decode_dnn.sh`

## Configuration

- `NUM_LAYERS = 2`
- `HIDDEN_DIM = 128`
- `EPOCHS = 25`
- `PATIENCE = 3`
- `BATCH_SIZE = 1024`
- `Optimizer`: Adam, lr=0.002, weight_decay=1e-5
- `Scheduler`: ReduceLROnPlateau, factor=0.1, patience=3

## Results

| Μοντέλο | PER (%) |
|---------|---------|
| Mono GMM-HMM (Unigram) | 52.59 |
| Mono GMM-HMM (Bigram) | 46.61 |
| Triphone GMM-HMM (Bigram) | 34.89 |
| DNN-HMM | 39.00 |

## Notes

- Εκπαίδευση σε CPU χωρίς GPU, χρησιμοποιήθηκε HIDDEN_DIM=128
- Early stopping ενεργοποιήθηκε στην 3η εποχή
- Καλύτερο αποτέλεσμα: wer_2_0.0 με PER 39.00%
