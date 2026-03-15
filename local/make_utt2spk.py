import os

# Ορισμός των ζευγών αρχείων εισόδου και εξόδου για το utt2spk
tasks = [
    ("../usc/filesets/validation.txt", "../data/dev/utt2spk"),
    ("../usc/filesets/testing.txt", "../data/test/utt2spk"),
    ("../usc/filesets/training.txt", "../data/train/utt2spk")
]

# Εκτέλεση της διαδικασίας για κάθε ζεύγος
for input_path, output_path in tasks:
    # Σιγουρευόμαστε ότι υπάρχουν οι φάκελοι data/train, data/dev κλπ
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(input_path, "r") as infile, open(output_path, "w") as outfile:
        for line in infile:
            utt_id = line.strip()
            if not utt_id:
                continue
            
            # Διαχωρισμός για να πάρουμε τον ομιλητή (π.χ. m1 από το m1_001)
            speaker_id = utt_id.split("_")[0]
            
            # Εγγραφή στο αρχείο εξόδου στη μορφή: utterance_id speaker_id
            outfile.write(f"{utt_id} {speaker_id}\n")

    # Εκτύπωση επιβεβαίωσης για κάθε αρχείο που ολοκληρώνεται
    print(f"Created: {output_path} from {input_path}")

print("\nΌλα τα utt2spk αρχεία δημιουργήθηκαν επιτυχώς!")