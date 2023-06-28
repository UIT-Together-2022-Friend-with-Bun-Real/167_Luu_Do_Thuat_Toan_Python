n = int(input("Nhap n: "))
s = 0
i = 1
while i < n:
    if n % i == 0:
        s = s + i
    i = i + 1
if s == n:
    kq = "La so HT"
else:
    kq = "Khong HT"
print(kq)
