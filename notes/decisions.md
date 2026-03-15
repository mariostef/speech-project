# Decisions

- The team repository will remain separate from the main Kaldi repository.
- The GitHub repository is the main shared project codebase.
- The repository structure is organized by assignment section/question.
- Each main assignment part gets its own script inside `questions/`.
- Dataset-specific helper scripts are stored in `local/`.
- Configuration files are stored in `conf/`.
- DNN-related files are stored in `dnn/`.
- Notes and report material are stored separately in `notes/` and `report/`.

## What is stored in the repository
- project scripts
- helper scripts
- configs
- notes
- report files

## What is not stored in the repository
- the full Kaldi installation
- the USC-TIMIT dataset
- generated outputs such as `exp/`, `mfcc/`, or model artifacts
- machine-specific local paths or personal environment files

## Collaboration model
- Each teammate uses their own local Kaldi setup.
- Each teammate uses their own local dataset copy.
- Shared work is synchronized through GitHub.
- Scripts should avoid hardcoded absolute paths whenever possible.# Decisions

- We will keep the team project in a separate Git repository at `~/speech-project`.
- We will not upload the full Kaldi directory.
- We will not upload the USC-TIMIT dataset.
- We will not upload generated directories such as `exp/`, `mfcc/`, or other large artifacts.
- We will keep scripts portable between WSL and Docker.
- We will avoid hardcoded absolute paths whenever possible.
- Local dataset paths should be passed as arguments or clearly documented.
