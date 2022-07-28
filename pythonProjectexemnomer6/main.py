a = input('Введите текс: ')

top = []
down = []
b = 0
c = 0

for i in a:
    if i.islower():
        down.append(i)
    if i.isupper():
        top.append(i)
    if i in 'ауоыэяюёиеАУОЫЭЯЮЁИЕaeyuioAEYUIO':
        b += 1
    else:
        c += 1

print('Количество пар c нижним регистром:', (len(down) // 2))
print('Количество пар с верхним регистром:', (len(top) // 2))
print('Количество букв в слове:', len(a))
print('Гласных букв:', b, 'Согласных букв:', c)