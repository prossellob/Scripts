from time import time
a = [5.76,4.7,25.3,4.6,32.4,55.3,52.3,7.6,7.3,86.7,43.5] # The list I'm going to sort.
b = [None] * len(a)
x = 0
print(a)
time1 = time()
for number in a:
    for num in a:
        if number >= num:
            x += 1
    b[x-1] = number
    x = 0
b = b[::-1]
for number in b:  #This part of the code is for the duplicated numbers.
    if number == None:
        b[b.index(number)] = b[b.index(number) - 1]
b = b[::-1]
time2 = time()
print(b)
print(time2 - time1)
