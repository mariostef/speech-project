import re
import os

# Διαδρομές για τα κοινά αρχεία
trans_path = "../usc/transcriptions.txt"
lexicon_path = "../usc/lexicon.txt"

# Ορισμός των ζευγών (αρχείο εισόδου split -> αρχείο εξόδου text)
tasks = [
    ("../usc/filesets/validation.txt", "../data/dev/text"),
    ("../usc/filesets/testing.txt", "../data/test/text"),
    ("../usc/filesets/training.txt", "../data/train/text")
]

def load_transcriptions(path):
    trans = {}
    with open(path) as f:
        for line in f:
            parts = line.strip().split(maxsplit=1)
            if len(parts) < 2: continue
            idx = parts[0]
            sentence = parts[1]
            trans[idx] = sentence
    return trans

def load_lexicon(path):
    lex = {}
    with open(path) as f:
        for line in f:
            parts = line.strip().split()
            if not parts: continue
            word = parts[0].lower()
            phones = parts[1:]
            lex[word] = phones
    return lex

def clean_sentence(sentence):
    sentence = sentence.lower()
    # Αφαίρεση συμβόλων εκτός από το single quote (')
    sentence = re.sub(r"[^\w\s']", "", sentence)
    words = sentence.split()
    return words

# Φορτώνουμε τα δεδομένα ΜΙΑ φορά
transcriptions = load_transcriptions(trans_path)
lexicon = load_lexicon(lexicon_path)

# Εκτέλεση για κάθε split
for input_path, output_path in tasks:
    # Δημιουργία φακέλου αν δεν υπάρχει
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(input_path) as f:
        utt_ids = [line.strip() for line in f if line.strip()]

    with open(output_path, "w") as out:
        for utt in utt_ids:
            # Παίρνουμε το νούμερο της πρότασης (π.χ. από m1_001 παίρνουμε το 001)
            sent_id = utt.split("_")[1]
            
            if sent_id in transcriptions:
                sentence = transcriptions[sent_id]
                words = clean_sentence(sentence)
                
                # Ξεκινάμε με sil
                phonemes = ["sil"]
                
                for w in words:
                    if w in lexicon:
                        phonemes.extend(lexicon[w])
                    # (Προαιρετικά: εδώ θα μπορούσες να βάλεις <unk> αν η λέξη λείπει)
                
                # Τελειώνουμε με sil
                phonemes.append("sil")
                
                out.write(f"{utt} {' '.join(phonemes)}\n")

    print(f"Created: {output_path} from {input_path}")

print("\nΌλα τα αρχεία text δημιουργήθηκαν επιτυχώς!")