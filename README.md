# Speech Processing Project

Phone recognition project based on Kaldi and USC-TIMIT.

## Repository purpose
This repository stores the team-managed project files for the lab assignment.

It includes:
- question-based scripts
- dataset-specific helper scripts
- configuration files
- notes
- report material

It does not include:
- the full Kaldi installation
- the USC-TIMIT dataset
- generated experiment outputs
- trained models
- large artifacts

## Repository structure

- `main.sh`  
  Entry point / top-level helper script.

- `path.sh`, `cmd.sh`  
  Standard Kaldi-style environment scripts.

- `questions/`  
  Main scripts organized by assignment section / question:
  - `prelab.sh`
  - `q1_perplexity.sh`
  - `q2_cmvn.sh`
  - `q3_features.sh`
  - `q4_mono_gmmhmm.sh`
  - `q5_bayes_decode.sh`
  - `q6_hclg.sh`
  - `q7_q8_dnn.sh`

- `local/`  
  Dataset-specific helper scripts:
  - `prepare_usc_data.sh`
  - `prepare_dict.sh`
  - `prepare_lm.sh`
  - `prepare_lang_fst.sh`
  - `text_to_phones.py`

- `conf/`  
  Configuration files such as `mfcc.conf`.

- `dnn/`  
  Files related to the optional DNN part.

- `notes/`  
  Team notes, decisions, and TODO items.

- `report/`  
  Report draft and final write-up material.

## Execution model
Each teammate keeps:
- their own local Kaldi installation
- their own local copy of the dataset

The shared GitHub repository stores:
- the project scripts
- configs
- notes
- report material

## Local environment
On the current setup:
- Kaldi root: `$KALDI_ROOT`
- USC example directory: `$KALDI_ROOT/egs/usc`

## Workflow
Typical workflow:
1. update or add project files in this repository
2. commit and push changes to GitHub
3. pull changes on the teammate's machine
4. run the project scripts on each teammate's own local Kaldi setup

## Notes
See `notes/` for:
- setup history
- project decisions
- pending tasks# Speech Processing Project

Phone recognition project using Kaldi and USC-TIMIT.

## Repository scope
This repository contains only project-specific files:
- scripts
- local preparation files
- configs
- notes
- report material

It does not contain:
- the full Kaldi installation
- datasets
- generated experiment outputs
- trained models

## Environment
- Teammate 1: WSL-based Kaldi installation
- Teammate 2: Docker-based Kaldi installation

The project must remain portable across both setups.

## Notes
See `notes/` for setup logs, decisions, and pending tasks.
