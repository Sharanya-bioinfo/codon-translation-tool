def validate_sequence(sequence):
    """Clean and validate a DNA or RNA sequence."""
    sequence = "".join(sequence.split()).upper()

    if not sequence:
        raise ValueError("Sequence cannot be empty.")

    if not set(sequence) <= set("ACGTU"):
        raise ValueError(
            "Sequence must contain only A, C, G, T or U."
        )

    if "T" in sequence and "U" in sequence:
        raise ValueError("Do not mix DNA base T and RNA base U.")

    return sequence


def split_codons(sequence):
    """Return complete triplets and any leftover bases."""
    complete_length = len(sequence) - (len(sequence) % 3)
    codons = [
        sequence[i:i + 3]
        for i in range(0, complete_length, 3)
    ]
    incomplete = sequence[complete_length:]

    return codons, incomplete


# Test block to run and test functions directly
if __name__ == "__main__":
    test_seq = "ATGGCCATG"  # Valid DNA sequence
    try:
        clean_seq = validate_sequence(test_seq)
        codons, leftover = split_codons(clean_seq)
        print("Cleaned Sequence:", clean_seq)
        print("Codons:", codons)
        print("Leftover:", leftover)
    except ValueError as e:
        print("Validation Error:", e)