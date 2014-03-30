import sys

# string1 = 'AAATAAA'
# string2 = 'AAATTTT'
# string3 = 'TTTTCCC'
# string4 = 'AAATCCC'
# string5 = 'GGGTGGG'
# string_list = [string1, string2, string3, string4, string5]

file = open(sys.argv[1], 'r')

def build_string_list(f):

	working_sequences = []
	sequences = []

	for line in f:
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


print build_string_list(file)


# for i in string_list:
#     for j in string_list:
#         if i != j:
# 			if i[:3] == j[-3:]:
# 				print '{0} {1}'.format(j, i)