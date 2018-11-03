# Special pythagorean triple
# Maybe find a way to create an algorithm for this!

k = 25
m = 4
n = 1

a = k * (m**2 - n**2)
b = k * (2 * m * n)
c = k * (m**2 + n**2)

print a
print b
print c
print "Sum: %d" % (a + b + c)
