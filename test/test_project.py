import unittest
from sequence_utils import validate_sequence, split_codons
from codon_table import CODON_TABLE
from translator import translate_sequence
from frameshift import simulate_frameshift
from codon_usage import calculate_codon_usage


class TestCodonTranslationTool(unittest.TestCase):

    def test_sequence_validation(self):
        self.assertEqual(validate_sequence("  atg gcc  "), "ATGGCC")
        with self.assertRaises(ValueError):
            validate_sequence("")
        with self.assertRaises(ValueError):
            validate_sequence("ATGCX")
        with self.assertRaises(ValueError):
            validate_sequence("ATGU")

    def test_split_codons(self):
        codons, incomplete = split_codons("ATGGCCATG")
        self.assertEqual(codons, ["ATG", "GCC", "ATG"])
        self.assertEqual(incomplete, "")

        codons, incomplete = split_codons("ATGGCCAT")
        self.assertEqual(codons, ["ATG", "GCC"])
        self.assertEqual(incomplete, "AT")

    def test_translation(self):
        result = translate_sequence("ATGGCCATGTAA")
        self.assertEqual(result["protein"], "MAM*")
        self.assertEqual(result["start_codons"], ["ATG", "ATG"])
        self.assertEqual(result["stop_codons"], ["TAA"])

    def test_frameshift_insertion(self):
        mutated = simulate_frameshift("ATGGCT", 2, "insert", "A")
        self.assertEqual(mutated, "AATGGCT")

    def test_frameshift_deletion(self):
        mutated = simulate_frameshift("ATGGCT", 2, "delete")
        self.assertEqual(mutated, "AGGCT")

    def test_codon_usage(self):
        result = calculate_codon_usage("ATGGCCATG")
        self.assertEqual(result["counts"]["ATG"], 2)
        self.assertEqual(result["counts"]["GCC"], 1)


if __name__ == "__main__":
    unittest.main()