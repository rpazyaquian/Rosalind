## Not working yet.

from __future__ import division

import sys

k = int(sys.argv[1])
m = int(sys.argv[2])
n = int(sys.argv[3])

homozygous_dominant = k
heterozygous = m
homozygous_recessive = n

prob_het_hd = (heterozygous/(homozygous_dominant+heterozygous+homozygous_recessive) * \
	homozygous_dominant/(homozygous_dominant+heterozygous+homozygous_recessive-1))

prob_hd_het = (homozygous_dominant/(homozygous_dominant+heterozygous+homozygous_recessive) * \
	heterozygous/(homozygous_dominant+heterozygous+homozygous_recessive-1))

prob_hd_hd = (homozygous_dominant/(homozygous_dominant+heterozygous+homozygous_recessive) * \
	homozygous_dominant/(homozygous_dominant+heterozygous+homozygous_recessive-1))

final_probability = prob_hd_het + prob_het_hd

print final_probability