print("Hello")
print("Python")
print("AATGGCCTGTTGG")
dna_seq="AATTGGCGTTATGCAATTGCCC" 
print(dna_seq)
print(len(dna_seq))
length=len(dna_seq)
print(dna_seq[:int(length/2)])
print(dna_seq[int(length/2):])
lower_dna_seq=dna_seq.lower()
print(lower_dna_seq)
print(dna_seq.count("A"))
print(dna_seq.find("T"))
gc_percentage= 100*(dna_seq.count("G")+dna_seq.count("C"))/len(dna_seq)
print(gc_percentage)
