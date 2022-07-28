import random
tip = 1
one = 0
two = 0
while tip <= 7:
    c = int(input("Введите первое число от 1 до 20: "))
    d = int(input("Введите второе число от 1 до 20: "))
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    print("Случайные числа: ", a, b)

    if c > a and d > b:
        one += 1
        print(one, "раз введенные числа больше случайных")
    else:
        two += 1
        tip += 1
    if one == two and tip == 4:
        print("Случайные числа :", a, b)
