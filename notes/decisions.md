# Decisions

- We will keep the team project in a separate Git repository at `~/speech-project`.
- We will not upload the full Kaldi directory.
- We will not upload the USC-TIMIT dataset.
- We will not upload generated directories such as `exp/`, `mfcc/`, or other large artifacts.
- We will keep scripts portable between WSL and Docker.
- We will avoid hardcoded absolute paths whenever possible.
- Local dataset paths should be passed as arguments or clearly documented.
