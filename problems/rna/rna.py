import sys
import re

f = open(sys.argv[1], 'r')

for line in f:
	s = line

	print re.sub('T', 'U', re.sub('t', 'u', s))