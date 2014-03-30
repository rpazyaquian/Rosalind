import sys

def find_consensus(profile_matrix):

	consensus = ''

	for i in range(len(profile_matrix[0]) - 1):
		winning_letter = 'A'
		high_score = 0
		for line in profile_matrix:
			if line[i+1] >= high_score:
				high_score = line[i+1]
				winning_letter = line[0]
		consensus = consensus + winning_letter

	return consensus

file = open(sys.argv[1], 'r')

dna_strings = []

profile_matrix = [['A'], ['C'], ['G'], ['T']]

for line in file:
	if line[0] == '>':
		dna_strings.append('\t')
	else:
		dna_strings.append(line.strip())

dna_strings = ''.join(dna_strings).lstrip().split('\t')

for i in range(len(dna_strings[0])):
	cross_section = ''
	for string in dna_strings:
		cross_section = cross_section + string[i]
	profile_matrix[0].append(cross_section.count('A'))
	profile_matrix[1].append(cross_section.count('C'))
	profile_matrix[2].append(cross_section.count('G'))
	profile_matrix[3].append(cross_section.count('T'))

print find_consensus(profile_matrix)

for line in profile_matrix:
	totals = [line[i+1] for i in range(len(profile_matrix[0]) - 1)]
	print '{0}: '.format(line[0]) + ' '.join(str(x) for x in totals)