n = int(input("Nhap n: "))
at = 2
i = 2
ahh = 0
while i <= n:
    ahh = at + 2*i + 1
    i = i + 1
    at = ahh
print("Ket qua: ", ahh)
