import sys
import itertools

# codon table

bases = ['u', 'c', 'a', 'g']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))

file = open(sys.argv[1], 'r')

for line in file:

	work_line = line

	for char in range(len(work_line)):
		if work_line[char] == 'A' and work_line[char+1] == 'U' and work_line[char+2] == 'G':
			codon_line = work_line[char:]
			codons = list(codon_table[codon_line[3*x:3*(x+1):1].lower()] for x in range((len(codon_line)/3)))
			break


print ''.join(codons).replace('*', '')