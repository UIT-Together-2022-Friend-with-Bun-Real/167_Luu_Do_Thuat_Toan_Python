n=float(input("Nhap n: "))
s=0
i=1
while (i<n):
    if (n%i==0):
        s+=i;
    i+=1
print("Tong cac uoc nho hon n la: " , s)
