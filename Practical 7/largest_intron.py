seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA' 
splice_donor = []
splice_acceptor = []

for i in range(len(seq)-1): # Use "for" to cut the sequence and find GT/AG
    if seq[i:i+2] == "GT":
        splice_donor.append(i)
        min_sequence = min(splice_donor)
    elif seq[i:i+2] == "AG":
        splice_acceptor.append(i)
        max_sequence = max(splice_acceptor)
if splice_donor and splice_acceptor: 
    if min_sequence < max_sequence: # Ensure that the sequence exists
        max_intron_length = max_sequence - min_sequence + 2 #
        print("The largest intron that can be possibly generated.")
        print(f"Sequence: ", seq[min_sequence:min_sequence+max_intron_length])
        print(f"Length:", max_intron_length,"bp")
    else:
        print("No Intron Sequence")

