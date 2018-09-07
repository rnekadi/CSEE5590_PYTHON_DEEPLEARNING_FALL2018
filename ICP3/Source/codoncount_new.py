
# Codon Sequence Count from tsv file

import csv

#codonseq = 'AAAGGGTTTAAA'
# Ask user input for the codon sequence
codonseq = input("enter a codon sequence: ")

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
print('The individual codon sequences are : ', codon)

with open('codon.tsv', 'r') as f:
    reader = csv.reader(f, dialect='excel-tab')
    d = {}
    for row in reader:
        k, v = row
        d[k] = v

# Defining new dictionary for value count as per the user input
k1 = {}
d1 = {}


# iterating through values from list and counting the input codon sequence
for j in codon:
    for k, v in d.items():
        if j == k:
            #k1[k] = k
            k1[v] = 1 + k1.get(v, 0)
            d1[k] = v

#print the user input and its count with the dictionary value
print(k1, 'where', d1)