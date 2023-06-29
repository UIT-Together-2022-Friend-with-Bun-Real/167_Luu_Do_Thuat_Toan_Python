n=int(input("Nhap vao so nguyen duong n: "))
le=0
m=n
if (n==0):
    print("So n khong phai la so co toan chu so le")

while (n>0):
    k=n%10
    if (k%2==0):
        le=1
        print("So n khong phai la so co toan chu so le")
        break
    n//=10
if (le!=1 & m!=0):
    print("So n la so co toan chu so le")

