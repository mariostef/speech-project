cd ~/speech-project
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
