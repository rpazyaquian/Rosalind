# Shamelessly taken from a StackExchange answer. This was totally out of my league...

import sys

n = int(sys.argv[1])
m = int(sys.argv[2])

def mortal_fib(n, m):

	f = [0]*(n+1)

	f[0] = 1

	for i in range(2, n+1):
		f[i] = f[i-2] + f[i-1] - f[i - m - 1]

	return f[n] + f[n-1]

print mortal_fib(n, m)