import math
n = int(input("Nhap n: "))
x = float(input("Nhap x: "))
s = 0.0
t = 1
for i in range(n):
    t = t * x
    s = s + math.sin(t)
print("Ket qua: ", s)