from sequence_utils import validate_sequence

def simulate_frameshift(sequence, position, operation, base=None):
    """Insert or delete one nucleotide at a 1-based position."""
    sequence = validate_sequence(sequence)
    operation = operation.lower()

    if not 1 <= position <= len(sequence) + (operation == "insert"):
        raise ValueError("Position is outside the valid range.")

    if operation == "insert":
        if base is None:
            raise ValueError("Provide a base to insert.")
        
        base = validate_sequence(base)

        if len(base) != 1:
            raise ValueError("Inserted base must be one nucleotide.")

        if (
            ("U" in sequence and "T" in base)
            or ("T" in sequence and "U" in base)
        ):
            raise ValueError("Use U for RNA or T for DNA consistently.")
            
        return sequence[:position - 1] + base + sequence[position - 1:]

    if operation == "delete":
        if position > len(sequence):
            raise ValueError("Cannot delete beyond the sequence.")
        return sequence[:position - 1] + sequence[position:]

    raise ValueError("Operation must be 'insert' or 'delete'.")


# Test block to run the frameshift simulation directly
if __name__ == "__main__":
    test_seq = "ATGGCCATG"
    try:
        inserted_result = simulate_frameshift(test_seq, position=4, operation="insert", base="A")
        print("After Insertion:", inserted_result)

        deleted_result = simulate_frameshift(test_seq, position=4, operation="delete")
        print("After Deletion:", deleted_result)

    except ValueError as e:
        print("Error:", e)