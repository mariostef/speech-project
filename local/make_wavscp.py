import os

# Η βασική διαδρομή των αρχείων ήχου
wavdir_path = "/opt/kaldi/egs/speech-project/usc/wav"

# Ορισμός των ζευγών (αρχείο uttids -> αρχείο wav.scp)
tasks = [
    ("../data/test/uttids", "../data/test/wav.scp"),
    ("../data/train/uttids", "../data/train/wav.scp"),
    ("../data/dev/uttids", "../data/dev/wav.scp")
]

# Εκτέλεση για κάθε ζεύγος
for uttids_path, output_path in tasks:
    # Δημιουργία του φακέλου εξόδου αν δεν υπάρχει
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(uttids_path, "r") as infile, open(output_path, "w") as outfile:
        for line in infile:
            utt_id = line.strip()
            if not utt_id:
                continue
            
            # Κατασκευή του path: ../usc/wav/m1_001.wav
            wav_path = os.path.join(wavdir_path, utt_id + ".wav")
            
            # Εγγραφή στη μορφή: utterance_id path_to_wav
            outfile.write(f"{utt_id} {wav_path}\n")
    
    # Σχόλιο επιβεβαίωσης για κάθε αρχείο
    print(f"Created: {output_path} from {uttids_path}")

print("\nΌλα τα wav.scp αρχεία δημιουργήθηκαν επιτυχώς!")