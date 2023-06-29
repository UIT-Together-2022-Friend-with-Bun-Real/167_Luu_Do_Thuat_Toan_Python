
s=0
e=1
dem=0
i=1
while (e>=10**(-6)):
    dem+=i
    e=1/dem
    s+=e
    i+=1
print("S(n) = ", s)
