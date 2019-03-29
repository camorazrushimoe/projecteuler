'''
Последовательность Фибоначчи определяется рекурсивным правилом:

Fn = Fn−1 + Fn−2, где F1 = 1 и F2 = 1.
Таким образом, первые 12 членов последовательности равны:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
Двенадцатый член F12 - первый член последовательности, который содержит три цифры.

Каков порядковый номер первого члена последовательности Фибоначчи, содержащего 1000 цифр?
'''

feb_num = [1, 1]

i = 0

# print(len(feb_num))

while len(feb_num) < 4782:
    v = feb_num[i] + feb_num[i+1]
    feb_num.append(v)
    i += 1
    #print(feb_num)


def check_len (num):
    return len(str(num))

print(feb_num[0:15])
print("Count of element in list: ", len(feb_num))
print("len of number: ", check_len(feb_num[-1]))
print("Answer is: ", feb_num.index(feb_num[-1]) + 1)
#4782

