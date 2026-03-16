import os

# Ορισμός των πηγών και των προορισμών
# (Πηγή αρχείου, Όνομα αρχείου εξόδου)
tasks = [
    ("../data/train/text", "../data/local/dict/lm_train.text"),
    ("../data/dev/text", "../data/local/dict/lm_dev.text"),
    ("../data/test/text", "../data/local/dict/lm_test.text")
]

def prepare_lm_file(input_path, output_path):

    with open(input_path, "r") as fin, open(output_path, "w") as fout:
        for line in fin:
            parts = line.strip().split()
            if len(parts) > 1:
                # parts[0] -> utterance_id (το πετάμε)
                # parts[1:] -> τα φωνήματα (τα κρατάμε)
                phones_only = " ".join(parts[1:])
                
                # Εγγραφή με τα απαραίτητα tags
                fout.write(f"<s> {phones_only} </s>\n")
    
    print(f"Δημιουργήθηκε το: {output_path}")

# Εκτέλεση για όλα τα tasks
for src, dest in tasks:
    prepare_lm_file(src, dest)

print("\nΌλα τα LM αρχεία είναι έτοιμα!")