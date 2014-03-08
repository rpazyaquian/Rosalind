import sys

def fib(n, k):
	if n == 1:
		return 1
	elif n == 2:
		return 1
	else:
		return fib(n-1, k) + k*fib(n-2, k)


print fib(int(sys.argv[1]), int(sys.argv[2]))