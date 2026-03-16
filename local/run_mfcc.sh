#!/bin/bash

. ./path.sh

mkdir mfcc
mkfir -p exp/make_mfcc   

for x in train dev test; do
    steps/make_mfcc.sh --nj 4 data/$x exp/make_mfcc/$x mfcc || exit 1;
    steps/compute_cmvn_stats.sh data/$x exp/make_mfcc/$x mfcc || exit 1;
    echo "--- Ολοκληρώθηκε το $x ---"
done