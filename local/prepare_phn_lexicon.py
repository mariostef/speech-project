import os

# Paths
nonsilence_file = "../data/local/dict/nonsilence_phones.txt"
output_lexicon = "../data/local/dict/lexicon.txt"

with open(nonsilence_file, "r") as f:
    phones = [line.strip() for line in f if line.strip()]

with open(output_lexicon, "w") as f:
    # Πρώτα ορίζουμε τη σιωπή: λέξη 'sil' -> ήχος 'sil'
    f.write("sil sil\n")
    
    # Μετά για κάθε φώνημα: λέξη 'phn' -> ήχος 'phn'
    for p in phones:
        f.write(f"{p} {p}\n")

print(f"Το νέο lexicon.txt δημιουργήθηκε στο {output_lexicon}")