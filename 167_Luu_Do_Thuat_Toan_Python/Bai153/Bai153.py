import random
n=int(input("Nhap so n byte can kiem tra: "))
x=256*n
y=256*(n-1)
val=random.randint(y, x)
print("So can kiem tra la: ", val)
flag = 1
while (val>1):
    du = val%5
    if(du!=0):
        flag =0
    val = val//5 
if (flag == 1):
    print("So nguyen", n ,"byte la dang 5^m")
else:
    print("So nguyen", n ,"byte khong la dang 5^m")
