# I get a lot of "maximum recursion depth" problems here. Help!

import sys

def fib(n, m):

	if m != 1:

		if n == 1:
			return 1
		elif n == 2:
			return 1
		elif n == 3:
			return 2
		else:
			return fib(n-m, m) + fib(n-(m-1), m)

	else:
		return 1


print fib(int(sys.argv[1]), int(sys.argv[2]))