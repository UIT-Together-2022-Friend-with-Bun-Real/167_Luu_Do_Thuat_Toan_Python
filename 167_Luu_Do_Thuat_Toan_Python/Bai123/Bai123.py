
import math
ab = 2
bb = 1 
i=2
n = int(input("Nhap n: "))
while (i <= n):
    an=3*bb+2*ab
    bn=ab+3*bb
    i += 1
    ab=an
    bb=bn

print("So hang thu n cua day la ")
print("a(n)= ", an)
print("b(n)= ", bn)



