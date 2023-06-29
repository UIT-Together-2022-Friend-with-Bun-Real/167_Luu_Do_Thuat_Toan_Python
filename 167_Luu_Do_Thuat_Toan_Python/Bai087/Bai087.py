x=float(input("Nhap gia tri bien x: "))
n=int(input("Nhap n: "))
s=0
for i in range (n+1):
    s+=(-1)**i*x**(2*i+1)
print("S(n) = ", s)
