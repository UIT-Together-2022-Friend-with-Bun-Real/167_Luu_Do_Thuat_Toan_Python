
import math
n = int(input("nhap n: "))
t = n
flag = 1
while (t>1):
    du = t%3
    if(du!=0):
        flag =0
    t = t//3 
if (flag == 1):
    print("n la dang 3^m")
else:
    print("n khong la dang 3^m")
