sequence="ATGCTGATAGATAGTAAAATATAAGCA"
print(sequence)
print(len(sequence))
#Exon of sequence located 3...9
exon_sequence=sequence[3:10]
print(exon_sequence)
#intron of sequence
intron_Sequence=sequence[10:13]
print(intron_Sequence)
#print gene in the right half and length of gene
gene=sequence[int(len(sequence)/2):]
print(gene, len(gene))
#CDS: In Left half part and length of cds
CDS_sequence=sequence[:int(len(sequence)/2)]
print(CDS_sequence, len(CDS_sequence))
#Mutation: 7th position
mutation_position= sequence[6]
print(mutation_position)
#find index of every occurance of AT
Number_of_index_AT=sequence.count("AT")
print(Number_of_index_AT)

index=0
index_AT=[]
last_index=-1
while index<len(sequence):
    domain_AT=sequence.find("AT",last_index+1)
    if domain_AT!=-1:
        index_AT.append(last_index)
        last_index=domain_AT
    index+=1
print(index_AT)




