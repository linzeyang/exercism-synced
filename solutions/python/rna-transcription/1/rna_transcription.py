def to_rna(dna_strand):
    return dna_strand.translate(dna_strand.maketrans({"G": "C", "C": "G", "T": "A", "A": "U"}))
