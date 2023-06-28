n = int(input("Nhap n: "))
count = 0
while n > 0:
    n = n // 10
    count = count + 1
print("So luong chu so: ", count)
