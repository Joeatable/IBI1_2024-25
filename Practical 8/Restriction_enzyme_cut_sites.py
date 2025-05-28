import re
import random

# Function to find all positions where a restriction enzyme sequence matches the DNA sequence
def find_restriction_sites(DNA_sequence, enzyme_sequence):
    # Convert both sequences to uppercase to avoid case mismatch
    DNA_sequence = DNA_sequence.upper()
    enzyme_sequence = enzyme_sequence.upper()

    # Validate that both sequences contain only valid DNA bases (A, C, G, T)
    if re.fullmatch(r'[ACGT]+', DNA_sequence) and re.fullmatch(r'[ACGT]+', enzyme_sequence):
        # Use regular expression to find all matches of enzyme sequence in the DNA sequence
        matches = list(re.finditer(enzyme_sequence, DNA_sequence))
        if matches:
            # Return a list of start positions (1-based index) where enzyme sequence matches
            positions = [match.start() + 1 for match in matches]
            return positions
        else:
            return "No matches found in DNA sequence."
    else:
        return "Error: sequence contains invalid characters."

# Example 1: 
nucleotides = ["A", 'T', 'G', 'C']
DNA_sequence_1 = ''.join(random.choice(nucleotides) for _ in range(200))  # Random 200 bp DNA sequence
enzyme_sequence_1 = ''.join(random.choice(nucleotides) for _ in range(4))  # Random 4 bp enzyme sequence
print("The positions within the DNA sequence where the restriction enzyme cuts is: ", find_restriction_sites(DNA_sequence_1, enzyme_sequence_1))

# Example 2: 
print(find_restriction_sites("ATGCGTACGTCGCGCGTACG", "CGT"))
