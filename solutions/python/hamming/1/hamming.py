def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    return len([tup for tup in zip(strand_a, strand_b) if tup[0] != tup[1]])
