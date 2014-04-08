from __future__ import division

from math import factorial

# import sys

def bernoulli(p, n, m):

	return (factorial(n) / (factorial(m) * factorial(n-m))) * (p**m) * (1-p)**(n-m)

print bernoulli(0.5, 10, 4)

# k = int(sys.argv[1])
# N = int(sys.argv[2])

# probability of ending up as AaBb at any level > 1:

# assume k = 2, N = 1

# gen 0: AaBb
# at any generation, the likelihood of having an Aa organism is: 

# total population of generation k: 2^k = 2^2 = 4

# probability of Aa * Aa = Aa is: 1/2

# probability of Gen1Org1 = Aa AND Bb = Gen1Org1 = Aa * Gen1Org1 = Bb, given AaBb*AaBb: (1/2)*(1/2) = 1/4
# probability of Gen1Org2 = AaBb: 1/4

# probability of Gen1Org1 AND Gen1Org2 = AaBb: (1/4)(1/4) = 1/16

# probability of Gen2Org1 = Aa: (1/2)*(1/2) (chance of other allele being Aa->Aa) + (1/4)(1/2) (chance of other allele being AA->Aa) + (1/4)(1/4)
# (chance of other allele being aa -> Aa) = (1/2*1/2) + (1/4) + (1/4*1/4) / 3
# probability of G2O1 = Bb = (1/2*1/2) + (1/4) + (1/4*1/4) / 3  (similar concept for Aa)
# probability of G2O1 = Aa AND Bb = (1/2*1/2) + (1/4) + (1/4*1/4) / 3 *  (1/2*1/2) + (1/4) + (1/4*1/4) / 3

# probability of any organism at gen k being AaBb = probability of G1O1 = AaBb = 1/4

def find_prob_AaBb(k, N):

	if N > 2**k:
		return 'N must be less than or equal to 2^k.'

	if k == 0:
		return 1
	elif k == 1:
		return (1/16)
	else:

		# the total population, t, at any generation k is 2^k.
		# for example, there are 4 members of generation 2, not counting the parents.
		# i.e. gen 0 = 1, gen 1 = 1*2 = 2, gen 2 = 2*2 = 4. 

		# for any given organism with one parent Aa (assumed true for all organisms), and another unknown parent, the probability of being Aa is:
		# (1/2) (probability that their precursor was Aa) * (1/2) (probability that they will be Aa after crossing) +
		# (1/4) (probability that their precursor was AA) * (1/2) (probability that they will be Aa after crossing) +
		# (1/4) (probability that their precursor was aa) * (1/4) (probability that they will be Aa after crossing)
		# all divided by 3.

		# for any given organism with one parent Bb (assumed true for all organisms), and another unknown parent, the probability of being Bb is:
		# (1/2) (probability that their precursor was Bb) * (1/2) (probability that they will be Bb after crossing) +
		# (1/4) (probability that their precursor was BB) * (1/2) (probability that they will be Bb after crossing) +
		# (1/4) (probability that their precursor was bb) * (1/4) (probability that they will be Bb after crossing)
		# all divided by 3.

		# for any given organism with one parent AaBb, and another unknown parent, the probability of being AaBb is:
		# Probability of Aa AND Bb = Probability of Aa, times Probability of Bb.
		# Therefore, probability of AaBb is:
		# (((1/2)*(1/2)+(1/4)*(1/2)+(1/4)*(1/4)) / 3)**2 = "full heterogeneous" probability

		hetero_prob = (((1/2)*(1/2)+(1/4)*(1/2)+(1/4)*(1/4)) / 3)**2		

		# The big question:
		# What is the probability of N successes out of 2^k total trials if p = hetero_prob = (((1/2)*(1/2)+(1/4)*(1/2)+(1/4)*(1/4)) / 3)**2 ?
		# Use Bernoulli distro:

		total_prob = 0

		for i in range(N, 2**k):
			total_prob += bernoulli(0.25, 2**k, N)

		return total_prob

print find_prob_AaBb(2, 1)