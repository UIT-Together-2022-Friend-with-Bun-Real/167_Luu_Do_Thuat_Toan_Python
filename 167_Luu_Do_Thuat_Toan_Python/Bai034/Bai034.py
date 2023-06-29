n = int(input("Nhap n: "))
s = 0
i = 1
while i <= 2*n + 1:
    s = s + i/(i+1)
    i = i + 2
print("S = ", s)
