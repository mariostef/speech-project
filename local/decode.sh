#!/bin/bash
. ./path.sh

echo "--- Ξεκινάει η αποκωδικοποίηση (Decoding) ---"

# 1. Bigram Decoding (Dev & Test)
echo "Running Bigram Decoding..."
steps/decode.sh --nj 4 exp/mono/graph_bg data/dev exp/mono/decode_dev_bg || exit 1;
steps/decode.sh --nj 4 exp/mono/graph_bg data/test exp/mono/decode_test_bg || exit 1;

# 2. Unigram Decoding (Dev & Test)
echo "Running Unigram Decoding..."
steps/decode.sh --nj 4 exp/mono/graph_ug data/dev exp/mono/decode_dev_ug || exit 1;
steps/decode.sh --nj 4 exp/mono/graph_ug data/test exp/mono/decode_test_ug || exit 1;

echo "--- Η αποκωδικοποίηση ολοκληρώθηκε! ---"

# Εμφάνιση των καλύτερων αποτελεσμάτων WER
echo "--- Αποτελέσματα WER ---"
for x in exp/mono/decode_*; do
  grep WER $x/wer_* | utils/best_wer.sh | sed "s|^|$x: |"
done