import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
x = int(sys.argv[4])
y = int(sys.argv[5])
z = int(sys.argv[6])

# a through z = # of couples with the following genotypes:


# AA-AA, i.e. a couples have this genotype
# AA-Aa, i.e. b couples have this genotype
# AA-aa
# Aa-Aa
# Aa-aa
# aa-aa

# each couple has this probability of outputting a dominant offspring:

pa = 1
pb = 1
pc = 1
px = 0.75
py = 0.5
pz = 0

E = 2*(pa*a) + 2*(pb*b) + 2*(pc*c) + 2*(px*x) + 2*(py*y) + 2*(pz*z)

print E