from string import maketrans
import sys

f = open(sys.argv[1], 'r')

def complement(s):
	complement_trans = maketrans(r'acgtuACGTU', r'tgcaaTGCAA')
	return s.translate(complement_trans)[::-1]

assert complement('AAAACCCGGT') == 'ACCGGGTTTT'

for line in f:
	print complement(line)