n = int(input("Nhap n: "))
at = 2
ahh = 0
i = 2
while i <=n:
    ahh = (at*at + 2)/(2*at)
    i = i + 1
    at = ahh
print("Ket qua: ", ahh)
