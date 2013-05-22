# Jason Judd Roth
# Project Euler - Problem 7
# May 22, 2013

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
# can see that the 6th prime is 13.

# What is the 10,001st prime number?

def isPrime(m, L):
	"""returns if m is Prime or not"""
	for p in L:
		if m < p**2:
			return True
		if m%p == 0:
			return False

# number of primes to find
n = 10001

# PrimeList is a list of all primes in the range 2 <= p <= sqrt(m)
PrimeList = [2]

m = 3
while len(PrimeList) < n:
	if (isPrime(m, PrimeList)):
		PrimeList.append(m)
	m += 1

print(PrimeList[len(PrimeList) - 1])
	