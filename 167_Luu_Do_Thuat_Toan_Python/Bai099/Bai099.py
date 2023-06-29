n=int(input("Nhap n: "))
s=0
for i in range (1, n+1):
    s=(s+i)**(1/(i+1))
print("S(n) = ", s)
