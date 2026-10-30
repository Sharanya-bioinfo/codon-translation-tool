#  From DNA to Protein: A Journey Through the Genetic Code

### A  bioinformatics project using Python

**What if a sequence of just four letters could tell a cell how to build a protein?**

That is one of the fascinating ideas behind molecular biology

DNA stores biological information using four nucleotide bases — A, T, G and C. But how does this information become a protein?

The answer lies in the **genetic code**

This project explores that journey through Python. It takes a nucleotide sequence, reads it in groups of three bases called codons, and translates those codons into their corresponding amino acids

The project also explores a few interesting questions

- What happens when a nucleotide is inserted or deleted?
- Why can a single-base change alter the reading frame?
- Do all synonymous codons occur equally often?
- How can Python help us understand the language of DNA?


---

##  1. The Science Behind the Project

Imagine DNA as a biological instruction book

It contains four chemical letters

| DNA base | Name |
|---|---|
| A | Adenine |
| T | Thymine |
| G | Guanine |
| C | Cytosine |

During translation, the genetic message is read in groups of three nucleotides. Each group of three is called a **codon**

There are four possible bases at each of the three positions

**4 × 4 × 4 = 64 possible codons**

These codons specify 20 standard amino acids or a translation stop signal

For example

| Codon | Meaning |
|---|---|
| ATG | Methionine (M) |
| GCT | Alanine (A) |
| TTT | Phenylalanine (F) |
| TAA | Stop |

A sequence such as

`ATGGCTTTTTAA`

is divided into

`ATG – GCT – TTT – TAA`

And translated into

`M – A – F – *`

The resulting protein notation is

**MAF***

The asterisk represents a stop signal, not an amino acid

This simple example is the central idea behind the project

---

##  2. What Does This Project Do?

The Codon Translation Tool is a Python application that demonstrates the basic computational steps involved in reading nucleotide sequences

It includes five main capabilities

### Feature 1 — The Complete Genetic Code

The program stores all 64 standard DNA codons in a Python dictionary

For example

```python
CODON_TABLE = {
    "ATG": "M",
    "GCT": "A",
    "TTT": "F",
    "TAA": "*"
}
```

The complete dictionary is available in `codon_table.py`

### Feature 2 — DNA and RNA Translation

The program accepts DNA or RNA sequences, checks the input, separates the sequence into codons, and translates them into amino-acid symbols

For example

**DNA input**

```text
ATGGCTTTTTAA
```

**RNA input**

```text
AUGGCUUUUUAA
```

Both sequences produce

```text
MAF*
```

RNA uses uracil (U) instead of thymine (T). The program converts RNA codons internally for lookup while preserving their original RNA labels in the displayed codon list

### Feature 3 — Start, Stop and Incomplete Codon Detection

The program identifies

- The standard start codon — ATG (AUG in RNA)
- The three standard stop codons — TAA, TAG and TGA (UAA, UAG and UGA in RNA)
- Any leftover nucleotides that cannot form a complete group of three

For example

```text
Input: ATGGCTT

Complete codons: ATG - GCT
Incomplete bases: T
```

Why does this matter?

Because codons are read in groups of three. A leftover nucleotide cannot form a complete codon by itself

### Feature 4 — Frameshift Mutation Simulator

What happens if one nucleotide is inserted or deleted?

The reading frame can change, causing the downstream codons to be interpreted differently

The program allows the user to

- Insert one nucleotide at a selected position
- Delete one nucleotide at a selected position
- Compare the original and altered sequences
- Compare their translated protein outputs

This is a simplified computational demonstration of a frameshift mutation

### Feature 5 — Codon Usage and RSCU Analysis

Different codons can specify the same amino acid. These are called synonymous codons

For example

- TTT codes for Phenylalanine
- TTC also codes for Phenylalanine

But are these codons always used equally often?

The project explores this using **Relative Synonymous Codon Usage (RSCU)**

\[
RSCU_i = \frac{X_i}{\left(\frac{1}{n}\sum_{j=1}^{n}X_j\right)}
\]

Where

- \(X_i\) = observed count of a particular codon
- \(n\) = number of synonymous codons for that amino acid
- The denominator represents the expected count if synonymous codons were used equally

**Understanding RSCU**

| RSCU value | Meaning |
|---|---|
| 1 | Observed usage equals the equal-usage expectation |
| Greater than 1 | More frequent than expected |
| Less than 1 | Less frequent than expected |
| 0 | Codon was not observed |

For example, if TTT and TTC each occur once, their RSCU values are both 1

This provides a simple introduction to codon usage analysis

---

##  3. How to Use the Program

The project runs through an interactive terminal menu

Start the application using

```bash
python main.py
```

On Windows, you can also use

```bash
py main.py
```

The program displays

```text
===== CODON TRANSLATION TOOL =====

1. Display all 64 codons
2. Translate DNA or RNA
3. Simulate a frameshift mutation
4. Calculate codon usage and RSCU
5. Exit

Choose an option (1-5):
```

Select the required option and follow the instructions

### Example — Translating a DNA sequence

Choose option 2 and enter

```text
ATGGCTTTTTAA
```

Expected output

```text
--- TRANSLATION RESULT ---

Sequence: ATGGCTTTTTAA

Codons: ATG - GCT - TTT - TAA

Amino acids: M - A - F - *

Protein: MAF*

Start codons: ['ATG']

Stop codons: ['TAA']

Incomplete bases: None
```

### Example — Understanding an incomplete sequence

Enter

```text
ATGGCTT
```

The program identifies two complete codons and one leftover nucleotide

```text
Codons: ATG - GCT
Incomplete bases: T
```

### Example — Frameshift simulation

Consider the original sequence

```text
ATGGCT
```

If one nucleotide is deleted at position 2, the sequence becomes

```text
AGGCT
```

The codon grouping changes

```text
Original: ATG - GCT
Mutated:  AGG
```

This illustrates how changing a single nucleotide can alter the downstream reading frame

---

##  4. Project Structure

The project is divided into smaller Python files so that each component has a specific responsibility

```text
codon-translation-tool/
│
├── main.py
├── codon_table.py
├── sequence_utils.py
├── translator.py
├── frameshift.py
├── codon_usage.py
├── README.md
├── .gitignore
│
└── test/
    └── test_project.py
```

| File | Responsibility |
|---|---|
| `main.py` | Runs the interactive menu |
| `codon_table.py` | Stores and displays the 64 codons |
| `sequence_utils.py` | Validates sequences and splits codons |
| `translator.py` | Converts codons into amino acids |
| `frameshift.py` | Simulates nucleotide insertion and deletion |
| `codon_usage.py` | Calculates codon counts and RSCU |
| `test/test_project.py` | Contains automated tests |
| `README.md` | Explains the project |
| `.gitignore` | Excludes unnecessary generated files |

---

##  5. Testing the Project

A bioinformatics program should not only produce an output; it should also be checked for correctness

The project uses Python's built-in `unittest` framework

The tests cover

- Whether all 64 codons are present
- Whether codons map to the correct amino-acid symbols
- Whether valid sequences are accepted
- Whether invalid sequences are rejected
- Whether mixed DNA and RNA bases are rejected
- Whether sequences are correctly divided into triplets
- Whether DNA and RNA translation work
- Whether frameshift insertions and deletions work
- Whether codon counts are calculated correctly
- Whether equal synonymous codon usage produces the expected RSCU values

Run the tests with

```bash
python -m unittest discover -s test -v
```

The terminal should report the individual test results and a final test summary

---

##  6. Tools and Technologies

| Tool | Purpose |
|---|---|
| Python 3 | Main programming language |
| Visual Studio Code | Writing and running the code |
| Git | Tracking project changes |
| GitHub | Hosting the project repository |
| `unittest` | Automated testing |

---



---

##  8. Scope and Limitations

### What this project can do

This project demonstrates how a DNA or RNA sequence can be divided into groups of three and translated into amino-acid symbols using the standard genetic code

It can also identify standard start and stop codons, report leftover bases, simulate a single-base insertion or deletion, and calculate codon frequency and RSCU

It is designed to help beginners understand how basic bioinformatics concepts can be implemented using Python

### What this project cannot do yet

This is a small educational project, not a complete tool for analysing real genes or predicting proteins

- It starts reading the sequence from the first nucleotide you enter. It does not automatically find the correct starting position of a gene
- It does not identify complete genes or all possible open reading frames
- It does not reproduce the entire process of protein synthesis inside a living cell
- It does not predict the three-dimensional structure or function of a protein
- It uses the standard genetic code and does not currently support alternative genetic codes used by some organisms
- Its RSCU calculation uses the sequence entered by the user and does not provide a complete comparison of codon preferences between organisms

**In simple terms:** The program helps us understand how nucleotide sequences are read and translated, but it does not replace advanced bioinformatics tools used for real-world genome and protein analysis

---

##  9. References and Further Reading

The following resources provide background information about the genetic code and bioinformatics

- **NCBI — The Genetic Codes**  
  https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi


- **GitHub — Genetic Code and Codon Table Repositories**  
  https://github.com/search?q=genetic+code+codon+table&type=repositories

*The codon-table comparison with a public GitHub repository should be documented after checking the actual codon mappings against a selected repository*

---

# 10. A Final Thought

A DNA sequence may look like a random arrangement of four letters, but hidden within it is a biological language

This project was a small attempt to understand that language using Python — starting with a simple codon dictionary and gradually building a tool that can translate sequences, simulate mutations, and explore codon usage

For me, the interesting part was not just getting the correct protein output. It was understanding why the output changes when even a single nucleotide changes

**From four letters to a protein sequence — that is the journey this project explores**

---

**Project:** Codon Translation Tool  
**Language:** Python  
**Area:** Bioinformatics
**Author** Sharanya.R (M.SC Bioinformatics and Biotechnology)