import sys

dataset = sys.argv[1]

a_count = dataset.lower().count('a')
c_count = dataset.lower().count('c')
g_count = dataset.lower().count('g')
t_count = dataset.lower().count('t')

print '{0} {1} {2} {3}'.format(a_count, c_count, g_count, t_count)