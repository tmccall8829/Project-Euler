def isPrime(n):
	div = 2 # Divisor
	hasDivisor = False
	while (hasDivisor == False and div < n):
		if n % div == 0:
			hasDivisor = True
		else:
			div += 1
	if div == n:
		print "%d is prime" % n
		return True

num = 1
numPrimes = 0
while numPrimes < 10002:
	if isPrime(num):
		numPrimes += 1
	num += 1

print "%d primes" % (numPrimes+1) # Added one because 1 is prime
