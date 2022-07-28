import random
chislo = int(input("введите количество чисел "))
inp_0 = [random.randint(0, 10000000) for i in range(chislo)]
print(inp_0)
inp_0 = str(inp_0)

inp_1 = str(input('Какую цифру будем искать?'))

count = 0

for i in inp_0:
    if i == str(inp_1):
        count += 1

print("цифра", inp_1, ",", count,"раз", )