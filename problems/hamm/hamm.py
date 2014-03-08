import sys

file = open(sys.argv[1], 'r')

differences = 0

strings = []

for line in file:
	string = str(line).rstrip()
	strings.append(string)

for i in range(len(strings[0])):
	if strings[0][i] != strings[1][i]:
		differences += 1

print differences