# Jason Judd Roth
# Project Euler - Problem 8
# May 22, 2013

# Find the greatest product of five consecutive digits in the 1000-digit number.

# Open file to read in numbers to list
L = []

with open("problem8.txt") as f:
	for line in f:
		for c in line:
			if c.isdigit():
				L.append(int(c))

maxProduct = 0
numDigitsToMul = 5

for i in range(len(L) - numDigitsToMul):
	product = 1
	for j in range(i, i + numDigitsToMul):
		product *= L[j]
	if product > maxProduct:
		maxProduct = product

print(maxProduct)
