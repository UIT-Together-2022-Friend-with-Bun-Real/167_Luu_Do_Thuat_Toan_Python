import math
n = int(input("Nhap n: "))
x = float(input("Nhap x: "))
s = 0
t = 1
m = 0
dau = -1
for i in range(n):
    t = t * x
    m = m + i + 1
    s = s + dau*t/m
    dau = - dau
print("Ket qua: ", s)
