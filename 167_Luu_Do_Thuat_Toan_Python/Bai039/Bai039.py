n=float(input("Nhap n: "))
s=1
i=1
while (i<=n):
    s*=(1+1/(i*i))
    i+=1
print("S(n) = " , s)

