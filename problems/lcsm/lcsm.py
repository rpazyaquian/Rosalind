import sys

file = open(sys.argv[1], 'r')

def build_sequence_list(f):

	lines_list = []

	for line in f:
		lines_list.append(line.rstrip())

	names_list = []

	for i in lines_list:
		if i.startswith('>'):
			names_list.append(i)

	strings_list = []

	for i in lines_list:
		if i.startswith('>'):
			strings_list.append('>')
		else:
			strings_list.append(i)

	final_strings_list = ''.join(strings_list).split('>')[1:]

	associated_list = []

	for i in range(len(names_list)):
		associated_list.append([names_list[i], final_strings_list[i]])

	return associated_list

