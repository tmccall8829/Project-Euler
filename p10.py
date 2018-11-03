def isPrime(n):
	if n == 2 or n == 3:
		return True
	if n % 2 == 0 or n < 2:
		return False
	for i in range(3, int(n**0.5) + 1, 2):
		if n % i == 0:
			return False
	return True

def sumPrimesBelow(n):
	i = 1
	primesToSum = []
	while i < n:
		print "Testing %d" % i
		if isPrime(i):
			primesToSum.append(i)
			i += 1
		else:
			i += 1

	print sum(primesToSum)

sumPrimesBelow(2000000)
