# Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
# Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

# def palindrome(p)
#     if p == 0

def check_num(i):
    i = str(i)
    if i == i[::-1]:
        return True
    else:
        return False


list = [100]
a = 101

while a < 1000:
    list.append(a)
    a += 1

print(list) # все трехзначные числа из условия

list_num = 0
print(list[-1]) # последнее трехзначное из условия


num_s = -1
num = list[num_s] * list[num_s]
# num = str(num) # сделать строкой

print(num) # 999 * 999
# print(num[::-1]) # читать стринг с другой стороны

while check_num(num) == False:
    num_s = num_s - 1
    num = list[num_s] * 993 # проблема в том что это число угадал подбором руками

print(num_s)
print(num)
print(list[num_s]) # 913 * 913 = 906609



