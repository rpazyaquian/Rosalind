from __future__ import print_function

import sys

string1 = sys.argv[1]
string2 = sys.argv[2]

if len(string2) > len(string1):
	print('{0} does not fit in {1}.'.format(string2, string1))
else:
	for i in range(len(string1)):
		if string1[i:i+len(string2)] == string2:
			print(i+1, end=' ')
	print('\r')