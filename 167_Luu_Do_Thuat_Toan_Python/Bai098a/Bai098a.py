

import math
n = float(input("Nhap n: "))
s = 0
i = 2
while(i<=n):
    s = math.pow((i+s), 1/i)
    i = i+1
   
print ("Tong can tinh: ", s)
