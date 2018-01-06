i = 100
j = 100
dromes = []
while i < 1000:
    while j < 1000:
        if str(i * j)[::-1] == str(i * j):
            dromes.append(i * j)
        j += 1
    j = 100 # to reset j value
    i += 1

dromes.sort()
print dromes[len(dromes)-1]
