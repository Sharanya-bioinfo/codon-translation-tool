from collections import Counter, defaultdict
from codon_table import CODON_TABLE
from sequence_utils import validate_sequence, split_codons


def calculate_codon_usage(sequence):
    """Calculate codon counts and RSCU values."""
    sequence = validate_sequence(sequence)
    codons, incomplete = split_codons(sequence)

    # Convert RNA codons to DNA labels for consistent counting.
    codons = [codon.replace("U", "T") for codon in codons]
    counts = Counter(codons)

    synonymous_groups = defaultdict(list)
    for codon, amino_acid in CODON_TABLE.items():
        synonymous_groups[amino_acid].append(codon)

    rscu = {}

    for amino_acid, group in synonymous_groups.items():
        total = sum(counts[codon] for codon in group)
        number_of_codons = len(group)

        for codon in group:
            if total == 0:
                rscu[codon] = 0.0
            else:
                expected = total / number_of_codons
                rscu[codon] = counts[codon] / expected

    return {
        "counts": counts,
        "rscu": rscu,
        "incomplete": incomplete,
    }


# Test block to run the codon usage calculator directly
if __name__ == "__main__":
    test_seq = "ATGGCCATGGCG"  # Valid test sequence
    try:
        result = calculate_codon_usage(test_seq)
        print("Codon Usage Results:")
        print("  Counts:", dict(result["counts"]))
        print("  Incomplete bases:", result["incomplete"])
        print("  RSCU sample (ATG):", result["rscu"].get("ATG"))
    except ValueError as e:
        print("Validation Error:", e)