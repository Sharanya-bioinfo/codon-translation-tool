from codon_table import CODON_TABLE, START_CODONS, STOP_CODONS
from sequence_utils import validate_sequence, split_codons


def translate_sequence(sequence):
    """Translate DNA or RNA into a protein sequence."""
    sequence = validate_sequence(sequence)
    codons, incomplete = split_codons(sequence)

    amino_acids = []
    starts = []
    stops = []

    for codon in codons:
        # Convert RNA U to DNA T for table lookup.
        lookup_codon = codon.replace("U", "T")
        amino_acid = CODON_TABLE[lookup_codon]
        amino_acids.append(amino_acid)

        if lookup_codon in START_CODONS:
            starts.append(codon)

        if lookup_codon in STOP_CODONS:
            stops.append(codon)

    return {
        "sequence": sequence,
        "codons": codons,
        "amino_acids": amino_acids,
        "protein": "".join(amino_acids),
        "start_codons": starts,
        "stop_codons": stops,
        "incomplete": incomplete,
    }


# Test block to run the translator directly
if __name__ == "__main__":
    test_seq = "ATGGCCATGTAA"  # Valid test sequence with a start and stop codon
    try:
        result = translate_sequence(test_seq)
        print("Translation Results:")
        for key, value in result.items():
            print(f"  {key}: {value}")
    except ValueError as e:
        print("Validation Error:", e)