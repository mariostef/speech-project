#!/bin/bash

. ./path.sh

# 1. Alignment των Training δεδομένων
# Χρησιμοποιούμε το mono μοντέλο για να βρούμε πού πέφτει κάθε φώνημα στον χρόνο.
echo "--- Starting Alignment ---"
steps/align_si.sh --nj 4 --cmd run.pl \
  data/train data/lang exp/mono exp/mono_ali || exit 1;

# 2. Εκπαίδευση Triphone Μοντέλου (tri1)
# Οι παράμετροι 2000 (leaves) και 10000 (gaussians) είναι ιδανικές για το μέγεθος του project σου.
echo "--- Starting Triphone Training (deltas) ---"
steps/train_deltas.sh --cmd run.pl 2000 10000 \
  data/train data/lang exp/mono_ali exp/tri1 || exit 1;

# 3. Δημιουργία Γράφου HCLG
# Τώρα ο γράφος θα βασίζεται στο νέο tri1 μοντέλο.
echo "--- Creating Triphone Graph ---"
utils/mkgraph.sh data/lang_test_bg exp/tri1 exp/tri1/graph_bg || exit 1;

# 4. Αποκωδικοποίηση (Decoding)
# Θα δούμε πόσο βελτιώθηκε το PER στο test set.
echo "--- Starting Decoding ---"
steps/decode.sh --nj 4 exp/tri1/graph_bg data/test exp/tri1/decode_test_bg || exit 1;

# 5. Εμφάνιση Αποτελεσμάτων
echo "--- Final PER Results ---"
grep WER exp/tri1/decode_test_bg/wer_* | utils/best_wer.sh