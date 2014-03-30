from __future__ import division

import sys

k = int(sys.argv[1])  # # of homozygous dominant
m = int(sys.argv[2])  # # of heterozygous
n = int(sys.argv[3])  # # of homozygous recessive

t = k + m + n  # total # of organisms

# Likelihood of a dominant allele given the first organism is:

# k = homozygous dominant

k_chance = (k/t) * ((k-1) + m + n)/(t-1)

# m = heterozygous

m_chance = (m/t) * (k + (m-1)*(3/4) + n*(2/4))/(t-1)

# n = homozygous recessive

n_chance = (n/t) * (k + m*(2/4) + (n-1)*(0))/(t-1)

# total chance of dominant allele in end organism

t_chance = k_chance + m_chance + n_chance

print round(t_chance, 5)