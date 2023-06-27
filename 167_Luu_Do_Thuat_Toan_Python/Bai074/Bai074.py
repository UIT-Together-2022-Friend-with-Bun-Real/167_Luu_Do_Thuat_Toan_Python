
import math
n = float(input("Nhap n: "))
x = float(input("Nhap x: "))
s = 0
t = 1
i = 1
while(i<=n):
    t = t * i
    s = s + math.pow(x, i)/t
    i = i+1
   
print ("Tong can tinh: ", s)
