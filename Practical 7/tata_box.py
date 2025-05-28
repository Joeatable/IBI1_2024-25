import re  # Import the regular expression module

# Pattern for matching the TATAWAW motif
tata_box = re.compile(r'TATA[AT]A[AT]')

# Pattern to extract gene ID from header line (e.g., ">YBR232C_mRNA ..." => "YBR232C")
gene_id_pattern = re.compile(r'^>([A-Z0-9]+)_')

# List to store matched gene entries as (gene_id, sequence)
matched_genes = []

# Open and read the FASTA file
with open("/Users/joey/Desktop/IBI1_2024-25/Practical 7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") as file:
    current_gene = None  # Store current gene ID
    current_seq = ""     # Store current gene sequence

    for line in file:
        line = line.strip()  # Remove leading/trailing whitespace

        if line.startswith(">"):  # Header line
            # Before reading next header, check previous gene
            if current_gene and tata_box.search(current_seq):
                matched_genes.append((current_gene, current_seq))

            # Extract new gene ID
            match = gene_id_pattern.match(line)
            current_gene = match.group(1) if match else None
            current_seq = ""  # Reset sequence

        else:
            current_seq += line  # Append sequence lines

    # Final gene after the loop
    if current_gene and tata_box.search(current_seq):
        matched_genes.append((current_gene, current_seq))

# Write results to output file (two-line format, no FASTA symbol)
with open("/Users/joey/Desktop/IBI1_2024-25/Practical 7/tata_genes.fa", "w") as out:
    for gene, seq in matched_genes:
        out.write(f">{gene}\n{seq}\n")

# Print summary
print(f"Finished! A total of {len(matched_genes)} genes with TATAWAW motif were written to 'tata_genes.fa'.")
