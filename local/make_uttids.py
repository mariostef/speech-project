# Ορίζουμε τα ζεύγη (input_path, output_path)
tasks = [
    ("../usc/filesets/validation.txt", "../data/dev/uttids"),
    ("../usc/filesets/training.txt", "../data/train/uttids"),
    ("../usc/filesets/testing.txt", "../data/test/uttids")
]

# Τρέχουμε την ίδια διαδικασία για κάθε ζευγάρι
for input_path, output_path in tasks:
    # Σιγουρευόμαστε ότι ο φάκελος εξόδου υπάρχει (π.χ. το data/dev/)
    import os
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(input_path, "r") as infile, open(output_path, "w") as outfile:
        for line in infile:
            utt_id = line.strip()
            if utt_id: # Αγνοούμε κενές γραμμές αν υπάρχουν
                outfile.write(f"{utt_id}\n")
    
    print(f"Created: {output_path} from {input_path}")

print("\nΌλα τα uttids αρχεία δημιουργήθηκαν επιτυχώς!")