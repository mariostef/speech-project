## 2026-03-14 — Prelab check

### What was done
- Added `questions/prelab.sh` as the script for the prelab stage
- Checked the local USC Kaldi example directory
- Verified that `data/train`, `data/dev`, and `data/test` exist
- Verified the presence of:
  - `uttids`
  - `utt2spk`
  - `wav.scp`
  - `text.words`
  - `text`

### Findings
- The basic prepared data structure already exists for train/dev/test
- `text.words` contains the original sentence text
- `text` already contains phone sequences
- `text` includes `sil` at the beginning and end of each utterance

### Conclusion
- The basic prelab data preparation appears to already be completed in the local USC example
- The next step is to move to Question 1 (lexicon / LM / perplexity)# Setup Log

## 2026-03-14

### What was done
- Identified the local Kaldi installation at `~/kaldi-work/kaldi`
- Identified the USC example directory at `~/kaldi-work/kaldi/egs/usc`
- Confirmed that the main Kaldi directory is already its own Git repository
- Created a separate team repository at `~/speech-project`
- Initialized Git locally and connected the repository to GitHub
- Created a question-based project structure
- Added the following top-level files:
  - `main.sh`
  - `path.sh`
  - `cmd.sh`
- Added the following directories:
  - `questions/`
  - `local/`
  - `conf/`
  - `dnn/`
  - `notes/`
  - `report/`
- Moved `text_to_phones.py` into `local/`

### Current structure
The repository is currently organized around:
- one script per assignment section/question in `questions/`
- dataset-specific helper scripts in `local/`
- report and notes stored separately

### Environment
- Local machine uses WSL
- GitHub repository is active and connected
- Kaldi execution remains outside the repository

### Notes
- The repository is now organized for collaboration between WSL and Docker-based environments.
- Shared code belongs in the repository.
- Local data, Kaldi installation files, and generated outputs stay outside the repository.cd ~/speech-project
nano notes/setup_log.md## 2026-03-14 (continued)

### What I did
- Copied `text_to_phones.py` from the local Kaldi USC example into `~/speech-project/scripts/`

### Why
- This script is project-specific and should be tracked in the shared GitHub repository.

### Notes
- Shared scripts should live in the repository.
- Kaldi installation files and local dataset files should remain outside the repository.# Setup Log

## 2026-03-14

### What I did
- Created a separate project repository at `~/speech-project`
- Initialized a local Git repository
- Created the folders `notes`, `scripts`, `local`, `conf`, `report`
- Added the initial `README.md`

### Environment
- Local machine uses WSL
- Kaldi is located at `~/kaldi-work/kaldi`
- The Kaldi USC example is located at `~/kaldi-work/kaldi/egs/usc`

### Notes
- The main Kaldi directory is already its own Git repository, so our team project should remain separate.
- The teammate uses Docker, so project files should avoid hardcoded absolute paths.

### Pending
- Fill in the remaining notes files
- Add `.gitignore`
- Make the first commit
- Connect the repository to GitHub
