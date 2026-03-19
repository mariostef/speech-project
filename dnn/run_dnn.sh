#!/usr/bin/env bash

DATA_PATH=./data/test
GRAPH_PATH=./exp/tri1/graph_bg
TEST_ALI_PATH=./exp/tri1_ali_test
OUT_DECODE_PATH=./exp/tri1/decode_test_dnn
CHECKPOINT_FILE=./best_usc_dnn.pt
DNN_OUT_FOLDER=./dnn_out

. ./path.sh

# Step 2: Compute CMVN stats
for set in train dev test; do
  compute-cmvn-stats --spk2utt=ark:data/${set}/spk2utt scp:data/${set}/feats.scp ark:data/${set}/${set}_cmvn_speaker.ark
  compute-cmvn-stats scp:data/${set}/feats.scp ark:data/${set}/${set}_cmvn_snt.ark
done

# Step 3+4: Train DNN
python timit_dnn.py $CHECKPOINT_FILE

# Step 5: Extract posteriors
python extract_posteriors.py $CHECKPOINT_FILE $DNN_OUT_FOLDER

# Step 6: Decode
chmod +x decode_dnn.sh
./decode_dnn.sh $GRAPH_PATH $DATA_PATH $TEST_ALI_PATH $OUT_DECODE_PATH "cat $DNN_OUT_FOLDER/posteriors.ark"
