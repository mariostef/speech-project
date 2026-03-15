#!/usr/bin/env bash
set -euo pipefail

: "${KALDI_ROOT:?set KALDI_ROOT first}"

ln -sfn "$KALDI_ROOT/egs/wsj/s5/steps" steps
ln -sfn "$KALDI_ROOT/egs/wsj/s5/utils" utils

mkdir -p local
ln -sfn ../steps/score_kaldi.sh local/score_kaldi.sh
