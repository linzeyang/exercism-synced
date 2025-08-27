MAPPING = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
}

STOP = {"UAA", "UAG", "UGA"}

def proteins(strand):
    out = []
    i = 0

    while i < len(strand):
        if (rna := strand[i: i + 3]) in STOP:
            return out

        out.append(MAPPING[rna])
        i += 3

    return out
