#!/bin/bash
source ./path.sh

# Δημιουργία των FSTs του λεξικού
utils/prepare_lang.sh data/local/dict "<oov>" data/local/lang data/lang