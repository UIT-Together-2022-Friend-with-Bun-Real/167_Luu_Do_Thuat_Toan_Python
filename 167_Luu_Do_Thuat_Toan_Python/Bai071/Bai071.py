n = int(input("Nhap n: "))
x = float(input("Nhap x: "))
s = 0.0
t = x
for i in range(n+1):
    s = s + t
    t = t * x * x
print("Ket qua: ", s)
