# Jason Judd Roth
# Project Euler - Problem 6
# May 17, 2013

# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.

# sumOfSq = 0
# sqOfSum = 0

# simple brute force
# for i in range(101):
	# sumOfSq += i**2
	# sqOfSum += i
# sqOfSum = sqOfSum**2

# NOTE
# (1 + 2 + ... + n)^2 = n^2 * (n + 1)^2 * 1/4
# 1^2 + 2^2 + ... + n^2 = n * (n + 1) * (2n + 1) * 1/6

n = 100
n = n * (n**2 - 1) * (3*n + 2) * (1/12)
print(n)