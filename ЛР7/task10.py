for число in range(1, 101):
    if число % 3 == 0 and число % 5 == 0:
        print("FizzBuzz, кратно и трём и пяти")
    elif число % 3 == 0:
        print("Fizz, кратно трём")
    elif число % 5 == 0:
        print("Buzz, кратно пяти")
    else:
        print(число, "не кратно ни трём, ни пяти")
