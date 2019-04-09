#Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство
#a2 + b2 = c2
#Например, 32 + 42 = 9 + 16 = 25 = 52.
#Существует только одна тройка Пифагора, для которой a + b + c = 1000.
#Найдите произведение abc.

import random

def pif_num (num):
    a = 2 * num
    a = a * a
    b = num * num
    b = b - 1
    b = b * b
    c = num * num
    c = c + 1
    c = c * c
    pif = [a, b, c]
    return pif

def r_pif_num (a):
    if a[0] + a[1] + a[2] == 1000:
        return True
    else:
        return False

#
# for x in range(100):
#   print(random.randint(1,101))

i = 2
r = []
while i < 100:
    x = pif_num(i)
    r.append(x)
    i += 1

print(r)

check = None
for a in range(1, 500):
    if check: break
    for b in range(1, 500):
        if check: break
        for c in range(1, 500):
            if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
                print(a, b, c)
                check = True
                break

print("Ответ: ", 200*375*425)