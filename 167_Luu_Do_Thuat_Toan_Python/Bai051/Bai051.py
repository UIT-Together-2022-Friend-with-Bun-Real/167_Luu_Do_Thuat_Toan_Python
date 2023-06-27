import math
n=float(input("Nhap n: "))
T=1;
i=1
while (i<=n):
    if (n%i==0):
        T*=i;
    i+=1
print("Tich cac uoc cua n la: " , T)
