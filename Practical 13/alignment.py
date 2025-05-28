from Bio import SeqIO
from Bio.Align import substitution_matrices

human_record = next(SeqIO.parse("/Users/joey/Desktop/IBI_2024-25/IBI1_2024-25/Practical 13/human.fasta", "fasta"))
mouse_record = next(SeqIO.parse("/Users/joey/Desktop/IBI_2024-25/IBI1_2024-25/Practical 13/mouse.fasta", "fasta"))
random_record = next(SeqIO.parse("/Users/joey/Desktop/IBI_2024-25/IBI1_2024-25/Practical 13/random.fasta", "fasta"))

human_seq = str(human_record.seq)
mouse_seq = str(mouse_record.seq)
random_seq = str(random_record.seq)


blosum62 = substitution_matrices.load("BLOSUM62")

score = 0
identity = 0
length = min(len(human_seq), len(mouse_seq))

for a1, a2 in zip(human_seq[:length], mouse_seq[:length]):
    if a1 == a2:
        identity += 1
    key = (a1, a2) if (a1, a2) in blosum62 else (a2, a1)
    score += blosum62.get(key, -4)
print(f"\n===== {human_record.id} vs {mouse_record.id} =====")
print(f"BLOSUM62 Score: {score}")
print(f"Percent Identity: {(identity / length) * 100:.2f}%")

score = 0
identity = 0
length = min(len(human_seq), len(random_seq))
for a1, a2 in zip(human_seq[:length], random_seq[:length]):
    if a1 == a2:
        identity += 1
    key = (a1, a2) if (a1, a2) in blosum62 else (a2, a1)
    score += blosum62.get(key, -4)
print(f"\n===== {human_record.id} vs {random_record.id} =====")
print(f"BLOSUM62 Score: {score}")
print(f"Percent Identity: {(identity / length) * 100:.2f}%")

score = 0
identity = 0
length = min(len(mouse_seq), len(random_seq))
for a1, a2 in zip(mouse_seq[:length], random_seq[:length]):
    if a1 == a2:
        identity += 1
    key = (a1, a2) if (a1, a2) in blosum62 else (a2, a1)
    score += blosum62.get(key, -4)
print(f"\n===== {mouse_record.id} vs {random_record.id} =====")
print(f"BLOSUM62 Score: {score}")
print(f"Percent Identity: {(identity / length) * 100:.2f}%")
