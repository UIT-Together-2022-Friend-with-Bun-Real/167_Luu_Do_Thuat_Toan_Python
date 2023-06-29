n = int(input("Nhap n: "))
min = 10
while n > 0:
    temp = n % 10
    if temp < min:
        min = temp
    n = n // 10
print("Chu so nho nhat cua n: ", min)
