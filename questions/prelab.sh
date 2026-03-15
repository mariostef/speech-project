#!/usr/bin/env bash

set -e

echo "=== PRELAB CHECK ==="

USC_EGS_DIR="${USC_EGS_DIR:-$HOME/kaldi-work/kaldi/egs/usc}"

echo "Using USC_EGS_DIR=$USC_EGS_DIR"
echo

if [ ! -d "$USC_EGS_DIR" ]; then
  echo "ERROR: USC Kaldi example directory not found."
  exit 1
fi

echo "Top-level structure:"
find "$USC_EGS_DIR" -maxdepth 2 | sort
echo

for split in train dev test; do
  echo "=== Checking data/$split ==="
  if [ -d "$USC_EGS_DIR/data/$split" ]; then
    ls "$USC_EGS_DIR/data/$split"
    echo
    echo "--- sample: uttids ---"
    head -n 3 "$USC_EGS_DIR/data/$split/uttids"
    echo
    echo "--- sample: utt2spk ---"
    head -n 3 "$USC_EGS_DIR/data/$split/utt2spk"
    echo
    echo "--- sample: wav.scp ---"
    head -n 3 "$USC_EGS_DIR/data/$split/wav.scp"
    echo
    echo "--- sample: text.words ---"
    head -n 3 "$USC_EGS_DIR/data/$split/text.words"
    echo
    echo "--- sample: text ---"
    head -n 3 "$USC_EGS_DIR/data/$split/text"
  else
    echo "Missing directory: $USC_EGS_DIR/data/$split"
  fi
  echo
done

echo "Prelab content check finished."
