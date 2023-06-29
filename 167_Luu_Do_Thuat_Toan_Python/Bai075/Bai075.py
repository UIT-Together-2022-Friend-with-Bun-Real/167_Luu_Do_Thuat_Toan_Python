
from platform import java_ver


x=float(input("Nhap gia tri bien x: "))
n=int(input("Nhap n: "))
s=1
for i in range (1, n+1):
    k=2*i
    t=1
    for j in range (1, k+1):
        t*=j
        print(j, " t= ",t)
    s+=x**k/t
    print(i, " s= ", s)
print("S(n) = ", s)
