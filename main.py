from codon_table import display_codon_table
from sequence_utils import validate_sequence
from translator import translate_sequence
from frameshift import simulate_frameshift
from codon_usage import calculate_codon_usage


def show_translation():
    sequence = input("Enter a DNA or RNA sequence: ")

    try:
        result = translate_sequence(sequence)

        print("\n--- TRANSLATION RESULT ---")
        print("Sequence:", result["sequence"])
        print("Codons:", " - ".join(result["codons"]))
        print("Amino acids:", " - ".join(result["amino_acids"]))
        print("Protein:", result["protein"])
        print("Start codons:", result["start_codons"] or "None found")
        print("Stop codons:", result["stop_codons"] or "None found")
        print("Incomplete bases:", result["incomplete"] or "None")

    except ValueError as error:
        print("Error:", error)


def show_frameshift():
    try:
        sequence = validate_sequence(input("Enter DNA/RNA sequence: "))
        operation = input("Type insert or delete: ").strip().lower()
        position = int(input("Enter position (starting from 1): "))

        base = None
        if operation == "insert":
            base = input("Enter the base to insert: ").strip().upper()

        mutated = simulate_frameshift(
            sequence, position, operation, base
        )

        original_result = translate_sequence(sequence)
        mutated_result = translate_sequence(mutated)

        print("\nOriginal sequence:", sequence)
        print("Original protein:", original_result["protein"])
        print("Mutated sequence:", mutated)
        print("Mutated protein:", mutated_result["protein"])

    except ValueError as error:
        print("Error:", error)


def show_codon_usage():
    sequence = input("Enter a DNA or RNA sequence: ")

    try:
        result = calculate_codon_usage(sequence)

        print("\n--- CODON COUNTS ---")
        for codon, count in sorted(result["counts"].items()):
            print(f"{codon}: {count}")

        print("\n--- RSCU VALUES ---")
        for codon, value in sorted(result["rscu"].items()):
            print(f"{codon}: {value:.2f}")

        print("Incomplete bases:", result["incomplete"] or "None")

    except ValueError as error:
        print("Error:", error)


def main():
    while True:
        print("\n===== CODON TRANSLATION TOOL =====")
        print("1. Display all 64 codons")
        print("2. Translate DNA or RNA")
        print("3. Simulate a frameshift mutation")
        print("4. Calculate codon usage and RSCU")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            display_codon_table()
        elif choice == "2":
            show_translation()
        elif choice == "3":
            show_frameshift()
        elif choice == "4":
            show_codon_usage()
        elif choice == "5":
            print("Thank you for using the tool!")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 5.")


if __name__ == "__main__":
    main()