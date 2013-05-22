# Jason Judd Roth
# Project Euler - Problem 4
# May 15, 2013

# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 * 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

largest = 0

for i in range(1000):
	for j in range(1000):
		product = str(i * j)
		if product == product[::-1]:
			if int(product) > largest:
				largest = int(product)

print(largest)
