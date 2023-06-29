
import math
n = int(input("Nhap n: "))
t = n
dn = 0
while (t!=0):
    dv = t%10
    dn = dn*10 + dv
    t = t//10
if (dn == n ):
    print ("n la so doi xung")
else:
    print("n la so khong doi xung")

