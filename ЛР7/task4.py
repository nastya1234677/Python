number = int(input("Введите целое число больше 1: "))
is_prime = True
for i in range(2, int(number**0.5) + 1):
    if number % i == 0:
        is_prime = False
        break
if is_prime:
    print("Число простое.")
else:
    print("Число не является простым.")
