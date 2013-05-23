# Jason Judd Roth
# Project Euler - Problem 10
# May 22, 2013

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

def isPrime(m, L):
	"""returns if m is Prime or not"""
	for p in L:
		if m < p**2:
			return True
		if m%p == 0:
			return False

# number of primes to find
n = 2000000

# PrimeList is a list of all primes in the range 2 <= p <= sqrt(m)
PrimeList = [2]

m = 3
while PrimeList[len(PrimeList) - 1] < n:
	if (isPrime(m, PrimeList)):
		if m > n:
			break
		PrimeList.append(m)
	m += 1

sum = 0
for i in PrimeList:
	sum += i

print(sum)