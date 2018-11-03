import time
import math

def getFactors(n):
	i = 2
	factors = [1]
	factors = [i for i in range(i,int(math.ceil((n**0.5+1)))) if n % i == 0]
	return factors

def genTriNums(n):
	for i in range(2,n):
		factors = getFactors(sum(range(1,i)))
		if len(factors) >= 300:
			print "%d factors = 300+" % sum(range(1,i))
		if len(factors) >= 400:
			print "%d factors = 400+" % sum(range(1,i))
		if len(factors) >= 500:
			print sum(range(1,i))
			print factors
			break

t0 = time.time()
genTriNums(100000)
t1 = time.time()
t = t1-t0

print "Time: %f" % t
