# Jason Judd Roth
# Project Euler - Problem 5
# May 15, 2013

# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?

low = 1
high = 20
num = 0
isDone = False

while not isDone:
	num += 20
	for i in range(low, high + 1):
		if num%i != 0:
			break
		if i == high:
			isDone = True

print(num)
