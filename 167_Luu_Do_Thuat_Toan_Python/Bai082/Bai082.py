import math as m
x = float(input("Nhap x: "))
n = int(input("Nhap n: "))
s = 0
t = 1
i = 1
while i <= n:
    t = t * m.sin(x)
    s = s + t
    i = i + 1
print("S = ", s)
