import re  # Import the regular expression module


tata_pattern = re.compile(r'TATA[AT]A[AT]')  # Pattern for the TATAWAW 
gene_pattern = re.compile(r'gene:([^\s]+)')  # Pattern to extract gene name from header line

valid_signals = {'GTAG', 'GCAG', 'ATAC'} # Define valid splice signals
signal = input("Please input splice signal (GTAG / GCAG / ATAC): ").strip().upper()


if signal not in valid_signals: # Check for valid input
    print("Error: only GTAG, GCAG, or ATAC are allowed.") # Print error message if invalid
    exit()

# Define regex patterns for each splice signal
splice_patterns = {
    'GTAG': re.compile(r'GT\S+AG'), # Patterns
    'GCAG': re.compile(r'GC\S+AG'),
    'ATAC': re.compile(r'AT\S+AC')
}
splice_regex = splice_patterns[signal]

tata_genes = {} # Dictionary to store matched genes with TATA box and splice signal
current_gene = None
current_seq = ""  # Initialize the current sequence to an empty string


# Read the fasta file line by line
with open("/Users/joey/Desktop/IBI1_2024-25/Practical 7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") as f:
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            # Save the previous gene if it matched both motifs
            if current_gene:
                if tata_pattern.search(current_seq) and splice_regex.search(current_seq): # Check for TATA box and splice signal in the sequence
                    tata_matches = tata_pattern.findall(current_seq)
                    tata_genes[current_gene] = (current_seq, len(tata_matches))

            match = gene_pattern.search(line)# Extract new gene name
            current_gene = match.group(1) if match else None
            current_seq = "" # Reset the current sequence
        else: # If the line is a sequence line, append the line to the current sequence
            current_seq += line

    # After the loop, process the last gene
    if current_gene:
        if tata_pattern.search(current_seq) and splice_regex.search(current_seq):
            tata_matches = tata_pattern.findall(current_seq)
            tata_genes[current_gene] = (current_seq, len(tata_matches))


output_file = f"/Users/joey/Desktop/IBI1_2024-25/Practical 7/{signal}_spliced_genes.fa"

with open(output_file, "w") as out: # Write matched genes to the output file
    for gene, (seq, count) in tata_genes.items():
        out.write(f">{gene} TATA_boxes:{count}\n{seq}\n")

print(f"Done! Found {len(tata_genes)} genes with TATA box and splice signal {signal}. Results saved to: {output_file}")
