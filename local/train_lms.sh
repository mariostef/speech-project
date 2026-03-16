#!/bin/bash

source ../path.sh

mkdir -p ../data/local/lm_tnp

echo "Δημιουργία Unigram..."
build-lm.sh -i ../data/local/dict/lm_train.text -n 1 -o ../data/local/lm_tmp/unigram.ilm.gz

echo "Δημιουργία Bigram..."
build-lm.sh -i ../data/local/dict/lm_train.text -n 2 -o ../data/local/lm_tmp/bigram.ilm.gz

echo "--- Η διαδικασία ολοκληρώθηκε! ---"
