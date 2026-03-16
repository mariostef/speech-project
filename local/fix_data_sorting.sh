#!/bin/bash
source ./path.sh

for x in train dev test; do
    echo "Sorting data in data/$x..."
    sort  data/$x/wav.scp -o data/$x/wav.scp
    sort  data/$x/text -o data/$x/text
    sort  data/$x/utt2spk -o data/$x/utt2spk
    # Δημιουργούμε και το spk2utt που το θέλει το Kaldi ταξινομημένο
    utils/utt2spk_to_spk2utt.pl data/$x/utt2spk > data/$x/spk2utt
done
