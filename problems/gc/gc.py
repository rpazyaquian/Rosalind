from __future__ import division

import sys
import itertools

file = open(sys.argv[1], 'r')

working_line = ''
name = ''

top_line = ''
top_line_gc_content = 0

working_sequences = []
sequences = []

for line in file:
	if line.startswith('>'):
		working_sequences = []
		name = ''
		working_line = ''
		name = ''.join(line[1:])
		working_sequences.append(name.rstrip())
		working_sequences.append(working_line.rstrip())
		sequences.append(working_sequences)
	else:
		working_sequences[1] += line.rstrip()

for sequence in sequences:
	name = sequence[0]
	gc_content = (sequence[1].upper().count('G') + sequence[1].upper().count('C')) / len(sequence[1]) * 100
	if gc_content > top_line_gc_content:
		top_line_gc_content = gc_content
		top_line = name
		

print top_line + '\n' + str(top_line_gc_content)