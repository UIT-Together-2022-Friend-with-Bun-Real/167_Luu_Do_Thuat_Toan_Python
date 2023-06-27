
import math
n = float(input("Nhap n: "))
x = float(input("Nhap x: "))
s = 0
t = 1
i = 0
while(i<=n):
    t = (i+1)* math.pow(x, i)
    s = s + t
    i = i+1
   
print ("Tong can tinh: ", s)
