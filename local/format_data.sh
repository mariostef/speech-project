#!/bin/bash
. ./path.sh

# Ορισμός φακέλων
lmdir=data/local/nist_lm


for lm_suffix in bg ug; do
  test=data/lang_test_${lm_suffix}
  mkdir -p $test
  cp -r data/lang/* $test
  
  # Μετατροπή ARPA σε G.fst
  gunzip -c $lmdir/lm_phone_${lm_suffix}.arpa.gz | \
    arpa2fst --disambig-symbol=#0 \
             --read-symbol-table=$test/words.txt - $test/G.fst
  
  # Έλεγχος ποιότητας
  echo "Checking G.fst for $lm_suffix"
  fstisstochastic $test/G.fst
done

echo "Succeeded in formatting data."