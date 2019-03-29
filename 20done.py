'''
n! означает n × (n − 1) × ... × 3 × 2 × 1

Например, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Найдите сумму цифр в числе 100!.
'''

#10!

i = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
print(i)


n = 100
factorial = 1
while n > 1:
    factorial *= n
    n -= 1

print(factorial)
factorial = str(factorial)
print("Длинна факториала: ", len(factorial))

print(factorial[0:10])

sum = 9
check_num = 0

while check_num < len(factorial) - 1:
    sum = sum + int(factorial[check_num + 1])
    check_num = check_num + 1

print("Сумма: ", sum)

