import re
from pathlib import Path

def load_lexicon(path):
    lex = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 2:
                word = parts[0].lower()
                phones = " ".join(parts[1:])
                lex[word] = phones
    return lex

def normalize_text(s):
    s = s.lower()
    s = re.sub(r"[^a-z' \t]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

def words_to_phones(words, lex):
    out = ["sil"]
    for w in words.split():
        if w in lex:
            out.extend(lex[w].split())
        else:
            out.append("<unk>")
    out.append("sil")
    return " ".join(out)

def convert_split(split, lex):
    in_path = Path(f"data/{split}/text.words")
    out_path = Path(f"data/{split}/text")
    with open(in_path, "r", encoding="utf-8") as fin, open(out_path, "w", encoding="utf-8") as fout:
        for line in fin:
            line = line.rstrip("\n")
            if not line.strip():
                continue
            utt, text = line.split(" ", 1)
            norm = normalize_text(text)
            phones = words_to_phones(norm, lex)
            fout.write(f"{utt} {phones}\n")

def main():
    lex = load_lexicon("usc/lexicon.txt")
    for split in ["train", "dev", "test"]:
        convert_split(split, lex)

if __name__ == "__main__":
    main()
