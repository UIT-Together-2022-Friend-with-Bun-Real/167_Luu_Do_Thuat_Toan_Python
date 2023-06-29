x=float(input("Nhap gia tri bien x: "))
n=int(input("Nhap n: "))
t=1
s=0
for i in range (n+1):
    t*=x+i
    s+=1/t
print("S(x,n) = ", s)