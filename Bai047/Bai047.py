import math
n = int(input("Nhap n: "))
s = 0
for i in range(n):
    s = s + math.sqrt(1 + 1 / ((i+1)*(i+1)) + 1 / ((i+2)*(i+2)))
print("Ket qua: " , s)
