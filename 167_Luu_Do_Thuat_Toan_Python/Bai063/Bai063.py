
n=int(input("Nhap vao so nguyen n: "))
T=1
while (n>0):
    k=n%10
    if (k%2!=0):
        T*=k
    n//=10
print("Tich cac chu so le cua so nguyen duong n la: ", T)
