a = [4,5,2,7]

for i in range(0,len(a) - 1): #Loop exterior
    for j in range(0,len(a) - 1 - i): #Loop interior bloqueando el ultimo numero.
        if a[j] > a[j + 1]:
            a[j],a[j + 1] = a[j + 1],a[j]
print(a)
