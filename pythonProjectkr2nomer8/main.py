f = open('123.txt', 'r')
sum = 0
n = 0
for s in f:
    s = s.split()
    d = int(s[2])
    sum += d
    n += 1
    if d < 3:
        print(s[0], s[1], s[2])
print('Средний балл %.2f' %(sum/n))
