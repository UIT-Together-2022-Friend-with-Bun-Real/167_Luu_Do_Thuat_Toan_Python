import math
n = int(input("Nhap n: "))
s = 0
for i in range(n):
    s = s + math.sqrt(i + 1 + s)
print("Ket qua: ", s)
