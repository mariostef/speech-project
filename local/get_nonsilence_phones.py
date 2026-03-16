# Διαδρομές
input_lexicon = "../usc/lexicon.txt"
output_file = "../data/local/dict/nonsilence_phones.txt"

# Σύνολο για να κρατάμε μόνο μοναδικά φωνήματα
phones = set()

with open(input_lexicon, "r") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) > 1:
            # Τα φωνήματα είναι όλα μετά την πρώτη στήλη
            current_phones = parts[1:]
            for p in current_phones:
                # Καθαρίζουμε τυχόν κενά και αγνοούμε το sil
                p = p.strip()
                if p and p.lower() != "sil":
                    phones.add(p)

# Ταξινόμηση αλφαβητικά
sorted_phones = sorted(list(phones))

# Εγγραφή στο αρχείο
with open(output_file, "w") as f:
    for p in sorted_phones:
        f.write(p + "\n")

print(f"Δημιουργήθηκε το {output_file} με {len(sorted_phones)} φωνήματα.")