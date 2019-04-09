# http://euler.jakumo.org/problems/view/14.html
'''
Следующая повторяющаяся последовательность определена для множества натуральных чисел:

n → n/2 (n - четное)
n → 3n + 1 (n - нечетное)

Используя описанное выше правило и начиная с 13, сгенерируется следующая последовательность:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
Получившаяся последовательность (начиная с 13 и заканчивая 1) содержит 10 элементов.
Хотя это до сих пор и не доказано (проблема Коллатца (Collatz)),
предполагается, что все сгенерированные таким образом последовательности оканчиваются на 1.

Какой начальный элемент меньше миллиона генерирует самую длинную последовательность?

Примечание: Следующие за первым элементы последовательности могут быть больше миллиона.
'''

# i = [333]
# o = 88
#
# while i[-1] != 1:
#     if o % 2 == 0:
#         i.append(int(o))
#         o = o / 2
#     else:
#         i.append(int(o))
#         o = o * 3 + 1
#
# i.remove(333)
# print(i)

def collatz_num (o):
    i = [333] #we delet this num in the end of function
    while i[-1] != 1:
        if o % 2 == 0:
            i.append(int(o))
            o = o / 2
        else:
            i.append(int(o))
            o = o * 3 + 1
    i.remove(333)
    return len(i)

print("len of it is: ", collatz_num(88))

test_num = 13
collatz_len = 0

while test_num < 1000000:
    if collatz_num(test_num) <= collatz_len:
        print("add +1 to test_num")
        print("check num: ", test_num)
        test_num += 1
    else:
        collatz_len = collatz_num(test_num)
        actual_num = test_num
        print("update max size: ", collatz_len)
        test_num += 1

print("Len of list: ", collatz_len)
print("Input num for this len: ", actual_num) #Answer is: 837799

