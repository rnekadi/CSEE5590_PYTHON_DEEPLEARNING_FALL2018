# Program to read DNA Codon Sequence and Split into individual Codon

# Fixed Codon Sequence

codonseq = 'AAAGGGTTTAAA'


# Define List to hold individual Codon

codon = []

# Defining function to to fill Codon list


def codonlist(seq):
    if len(seq) % 3 == 0:
        for i in range(0, len(seq), 3):
            codon.append(seq[i:i+3])
        print()


# Calling Codonlist function

codonlist(codonseq)

# Output
print('The input Sequence is ', codonseq)
print('The individual codon sequence are : ', codon)








