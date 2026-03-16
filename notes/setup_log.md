## 2026-03-15 — Make symlinks portable

### What was done
- Added `local/setup_links.sh` to generate `steps`, `utils`, `local/score_kaldi.sh` from `KALDI_ROOT`
- Added symlinks to `.gitignore` so they are not versioned
- Removed symlinks from the repo to avoid hardcoded paths

### Notes
- Each teammate must set `KALDI_ROOT` and run `local/setup_links.sh`

## 2026-03-15 — Step 4.1.1 setup

### What was done
- Copied `path.sh` and `cmd.sh` from `egs/wsj/s5`
- Set `KALDI_ROOT` in `path.sh` with a portable fallback
- Set `train_cmd`, `decode_cmd`, `cuda_cmd` to `run.pl`
- Added symlinks `steps` and `utils` to `wsj/s5`
- Added `local/score_kaldi.sh` symlink
- Added `conf/mfcc.conf` from `wsj/s5/conf`
- Created language folders: `data/lang`, `data/local/dict`, `data/local/lm_tmp`, `data/local/nist_lm`

### Notes
- Teammate should export their own `KALDI_ROOT` in their shell

## 2026-03-15 — Step 4.1.1 setup

### What was done
- Copied `path.sh` and `cmd.sh` from `egs/wsj/s5`
- Set `KALDI_ROOT` in `path.sh` with a portable fallback
- Set `train_cmd`, `decode_cmd`, `cuda_cmd` to `run.pl`
- Added symlinks `steps` and `utils` to `wsj/s5`
- Added `local/score_kaldi.sh` symlink
- Added `conf/mfcc.conf` from `wsj/s5/conf`
- Created language folders: `data/lang`, `data/local/dict`, `data/local/lm_tmp`, `data/local/nist_lm`

### Notes
- Teammate should export their own `KALDI_ROOT` in their shell

## 2026-03-15 — Step 4.1.1 setup

### What was done
- Copied `path.sh` and `cmd.sh` from `egs/wsj/s5`
- Set `KALDI_ROOT` in `path.sh` with a portable fallback
- Set `train_cmd`, `decode_cmd`, `cuda_cmd` to `run.pl`
- Added symlinks `steps` and `utils` to `wsj/s5`
- Added `local/score_kaldi.sh` symlink
- Added `conf/mfcc.conf` from `wsj/s5/conf`
- Created language folders: `data/lang`, `data/local/dict`, `data/local/lm_tmp`, `data/local/nist_lm`

### Notes
- Teammate should export their own `KALDI_ROOT` in their shell

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
- Identified the local Kaldi installation at `$KALDI_ROOT`
- Identified the USC example directory at `$KALDI_ROOT/egs/usc`
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
- Kaldi is located at `$KALDI_ROOT`
- The Kaldi USC example is located at `$KALDI_ROOT/egs/usc`

### Notes
- The main Kaldi directory is already its own Git repository, so our team project should remain separate.
- The teammate uses Docker, so project files should avoid hardcoded absolute paths.

### Pending
- Fill in the remaining notes files
- Add `.gitignore`
- Make the first commit
- Connect the repository to GitHub



## 2026-03-15 — Prelab Preparation: Data Scripts & Local Setup

### What was done
- Placed the provided dataset into `usc/`.
- Updated `.gitignore` to ignore the `usc/` folder and all generated data folders (`data/train/`, `data/dev/`, `data/test/`) to ensure no local data or large index files are pushed to the repository.
- Developed 4 standalone Python scripts in `local/` to handle the **Prelab Preparation** requirements:
    - `make_uttids.py`
    - `make_utt2spk.py`
    - `make_wavscp.py`
    - `make_text.py`

### Important Notes for Teammates
- **Manual Path Configuration:** Each teammate must manually update the path variables at the beginning of these 4 scripts to match their local environment (Docker vs. WSL) before execution.
- **Absolute Paths in wav.scp:** The `make_wavscp.py` script is designed to generate **absolute paths** for each `.wav` file. Absolute paths are mandatory for Kaldi to function correctly; relative paths will cause execution errors.
- **Prelab Status:** All required Prelab files (`uttids`, `utt2spk`, `wav.scp`, `text`) have been successfully generated locally. The project is now ready to move to the main questions (Lexicon/LM).

## 2026-03-16 — Step 4.2: Language Model Preparation

### Step 1: Dictionary Preparation (data/local/dict)
**What was done:**
* **Silence Phones:** Created `silence_phones.txt` and `optional_silence.txt` in `data/local/dict/` containing the `sil` phoneme.
* **Nonsilence Phones:** Developed and executed `local/get_nonsilence_phones.py`. The script extracts unique phonemes from the original dataset lexicon (excluding `sil`) and saves them alphabetized in `nonsilence_phones.txt`.
* **Phoneme Lexicon:** Developed and executed `local/prepare_phn_lexicon.py`. This creates a new `lexicon.txt` for phoneme recognition where each phoneme maps to itself (1-1 mapping), including the `sil sil` entry.
* **LM Text Preparation:** Developed and executed `local/prepare_lm_text.py`. The script processes the `text` files for train, dev, and test sets by stripping utterance IDs and wrapping the phoneme sequences with `<s>` and `</s>` tags.
* **Extra Questions:** Created the required empty `extra_questions.txt` file using the `touch` command.

**Execution (from project root):**
1. `echo "sil" > data/local/dict/silence_phones.txt`
2. `echo "sil" > data/local/dict/optional_silence.txt`
3. `touch data/local/dict/extra_questions.txt`

**Python Script Execution (run from local/ directory due to relative paths):**
1. `cd local`
2. `python3 get_nonsilence_phones.py`
3. `python3 prepare_phn_lexicon.py`
4. `python3 prepare_lm_text.py`

### Step 2: Generation of Intermediate Language Model Format
**What was done:**
* **Automation:** Created the bash script `local/train_lms.sh` to automate the production of Unigram and Bigram models using the IRSTLM toolkit.
* **File Generation:** Generated the intermediate `.ilm.gz` files.
* **Output Files:** * `unigram.ilm.gz` (Order n=1)
    * `bigram.ilm.gz` (Order n=2)

**Execution (from the local/ directory):**
1. `chmod +x train_lms.sh`
2. `./train_lms.sh`

**Note for the team:** > If the `build-lm.sh` command returns a "command not found" error, it means the Docker environment does not have IRSTLM in its automatic Path or it hasn't been installed correctly. Ensure you have sourced `path.sh`.

### Step 3: Compilation of Language Models to ARPA Format
**What was done:**
* **Automation:** Created a bash script `local/compile_arpa_lms.sh` to convert the intermediate `.ilm.gz` files into the final ARPA format.
* **Filtering:** Used `grep -v unk` during compilation to remove unknown word tags, ensuring the phoneme-based models remain clean.
* **Storage:** The compiled models were stored in `data/local/nist_lm/`.
* **Output Files:**
    * `lm_phone_ug.arpa.gz` (Unigram ARPA)
    * `lm_phone_bg.arpa.gz` (Bigram ARPA)

**Execution (from the local/ directory):**
1. `chmod +x compile_arpa_lms.sh`
2. `./compile_arpa_lms.sh`

**Note:** Sourcing `path.sh` inside the script ensures that the IRSTLM `compile-lm` utility is accessible during execution.

### Step 4: Creation of Lang Directory and L.fst
**What was done:**
* **FST Generation:** Developed the `local/prepare_lang.sh` script to automate the setup of the `data/lang` directory.
* **Processing:** Utilized the Kaldi utility `utils/prepare_lang.sh`. The script takes the prepared dictionary from `data/local/dict`, defines the Out-Of-Vocabulary (`<oov>`) symbol, and generates the necessary files in `data/lang`.
* **Result:** Successfully created `L.fst`, which represents the lexicon as a Finite State Transducer.

**Execution (from project root):**
1. `chmod +x local/prepare_lang.sh`
2. `./local/prepare_lang.sh`

**Note:** The script sources `path.sh` to ensure that Kaldi binaries and `utils/` scripts are within the environment's execution path.


### Steps 5 & 6: Data Sorting and spk2utt Generation
**What was done:**
* **Data Sorting:** Developed the `local/fix_data_sorting.sh` bash script to automate the alphabetical sorting of `wav.scp`, `text`, and `utt2spk` files.
* **Batch Processing:** The sorting process was applied to all data splits: `train`, `dev`, and `test`.
* **Speaker-to-Utterance Mapping:** Utilized the Kaldi utility `utils/utt2spk_to_spk2utt.pl` to generate `spk2utt` files, which map each speaker to their corresponding utterances.

**Execution (from project root):**
1. `chmod +x local/fix_data_sorting.sh`
2. `./local/fix_data_sorting.sh`

**Note:** Sorting is mandatory in Kaldi (files must be C-sorted) to prevent errors in subsequent training and decoding stages.

### Step 7: Creation of the Grammar FST (G.fst)
**What was done:**
* **G.fst Generation:** Developed the `local/format_data.sh` script, following the TIMIT recipe logic. This script converts the ARPA language models (Unigram and Bigram) into Finite State Transducer (FST) format.
* **Process:**
    * Created dedicated test directories: `data/lang_test_ug` and `data/lang_test_bg`.
    * Utilized the `arpa2fst` utility to transform `.arpa.gz` files into `G.fst`.
    * Ran `fstisstochastic` to verify that the resulting FSTs are properly normalized (stochastic).
* **Result:** Successfully prepared the language directories required for the decoding phase.

**Execution (from project root):**
1. `chmod +x local/format_data.sh`
2. `./local/format_data.sh`

**Note:** The `--disambig-symbol=#0` flag is used to handle backoff transitions correctly and ensure the FST composition is valid.



### Question 1: Perplexity Evaluation

**What was done:**
Evaluation of the generated Unigram and Bigram language models by calculating their Perplexity (PP) on the validation and test sets.

**Execution (from project root):**
1. `compile-lm data/local/lm_tmp/unigram.ilm.gz --eval=data/local/dict/lm_dev.text`
2. `compile-lm data/local/lm_tmp/unigram.ilm.gz --eval=data/local/dict/lm_test.text`
3. `compile-lm data/local/lm_tmp/bigram.ilm.gz --eval=data/local/dict/lm_dev.text`
4. `compile-lm data/local/lm_tmp/bigram.ilm.gz --eval=data/local/dict/lm_test.text`

**Results:**

| Model | Dataset | Perplexity (PP) |
| :--- | :--- | :--- |
| **Unigram** | Validation (dev) | **32.43** |
| **Unigram** | Test | **31.99** |
| **Bigram** | Validation (dev) | **17.06** |
| **Bigram** | Test | **16.90** |

**Conclusion:**
The Bigram model reduces perplexity by approximately 50% compared to the Unigram, indicating that phoneme context significantly improves the model's predictive accuracy.

## 4.3 Feature Extraction (MFCCs)

### Step 8: MFCC Extraction & CMVN Stats
**What was done:**
* **Automation:** Developed the `local/run_mfcc.sh` script to automate the extraction of Mel-Frequency Cepstral Coefficients (MFCCs) for the `train`, `dev`, and `test` sets.
* **Normalization:** Applied Cepstral Mean and Variance Normalization (CMVN) to ensure the features are robust against different recording conditions.
* **Storage:** Extracted features are stored in `.ark` files, with `.scp` files acting as pointers to individual utterances.

**Execution (from project root):**
1. `chmod +x local/run_mfcc.sh`
2. `./local/run_mfcc.sh`

---

### Question 3: Acoustic Frames & Feature Dimension

**What was done:**
Used Kaldi utilities to determine the dimensionality of the extracted features and the number of acoustic frames for the first 5 utterances of the training set.

**Execution (from project root):**
1. `feat-to-dim scp:data/train/feats.scp -`
2. `feat-to-len scp:data/train/feats.scp ark,t:- | head -n 5`

**Results:**

| Property | Value / Utterance ID | Count / Dimension |
| :--- | :--- | :--- |
| **Feature Dimension** | All utterances | **13** |
| **Frames (1st)** | `f1_003` | **317** |
| **Frames (2nd)** | `f1_004` | **371** |
| **Frames (3rd)** | `f1_005` | **399** |
| **Frames (4th)** | `f1_007` | **328** |
| **Frames (5th)** | `f1_008` | **464** |