# Jason Judd Roth
# Project Euler - Problem 9
# May 22, 2013

# A Pythagorean triplet is a set of three natural numbers, a < b < c,
# for which, a^2 + b^2 = c^2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Starting with these two known facts, a^2 + b^2 = c^2 and that a + b + c = 1000
# we can solve for c = 1000 - (a + b) and plug into the other equation and
# through some algebra, get it down to

# a = (500000 - 1000b) / (1000 - b)

import math

a = 0
b = 0
# find b where a is a natural number
for i in range(1, 1000):
	b = i
	a = (500000 - 1000 * b) / (1000 - b)
	if math.floor(a) == a:
		break

print(a)
print(b)
c = 1000 - a - b
print(c)
print(a * b * c)