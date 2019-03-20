# 2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
# Какое самое маленькое число делится нацело на все числа от 1 до 20?

# 232792560 - на 19

def check_num(i): #проверяет деление без остатка на числа от 1 до 20
    a = 1
    while a < 21:
        if i % a == 0:
            b = True
            a = a + 1
        else:
            b = False
            return b
    return b


# list = []
# a = 12000000
# while a < 280000000:
#    list.append(a)
#    a += 1

current_num = 232792550

while check_num(current_num) != True:
    current_num = current_num + 1

print(current_num)





