# TODO

## Repository cleanup and structure
- [ ] Confirm that the current repository structure is final
- [ ] Decide whether any remaining legacy files/folders should be removed
- [ ] Keep README and notes aligned with the current structure

## Prelab
- [x] Inspect the USC Kaldi example structure
- [x] Verify train/dev/test prepared files
- [x] Verify `uttids`, `utt2spk`, `wav.scp`, `text.words`, `text`
- [x] Confirm that `text.words` contains sentence text
- [x] Confirm that `text` contains phone sequences with `sil`
- [ ] Decide whether any additional prelab generation script is needed
- [ ] Document the prelab findings in the report

## Question 1
- [ ] Prepare dictionary files
- [ ] Prepare LM input text
- [ ] Build unigram and bigram language models
- [ ] Calculate perplexity for validation and test sets
- [ ] Record results in the report

## Question 2
- [ ] Run or inspect CMVN-related steps
- [ ] Write the theoretical explanation of CMVN in the report

## Question 3
- [ ] Extract MFCC features
- [ ] Measure frame counts for the first 5 train utterances
- [ ] Record feature dimensionality
- [ ] Add results to the report

## Question 4
- [ ] Train monophone model
- [ ] Write explanation of GMM-HMM and monophone training

## Question 5
- [ ] Connect decoding results with Bayes-rule interpretation
- [ ] Write the theoretical answer in the report

## Question 6
- [ ] Prepare language/graph-related steps
- [ ] Write the HCLG explanation in the report

## Question 7-8 (bonus)
- [ ] Inspect DNN requirements
- [ ] Prepare optional DNN pipeline
- [ ] Write bonus answers if completed# TODO

## Immediate
- [ ] Add `.gitignore`
- [ ] Make first commit
- [ ] Create remote GitHub repository
- [ ] Add collaborator
- [ ] Document how project files relate to the Kaldi USC example

## Next
- [ ] Decide which files from `~/kaldi-work/kaldi/egs/usc` should be copied or referenced
- [ ] Add project scripts
- [ ] Add configuration files
- [ ] Start data preparation workflow
