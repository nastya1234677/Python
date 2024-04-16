number = int(input("Введите неотрицательное целое число: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print("Факториал числа:", factorial)
