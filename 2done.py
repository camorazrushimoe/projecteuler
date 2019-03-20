def fib(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        lst = fib(n-1)
        lst.append(lst[-1] + lst[-2])
        return lst


fib_num = fib(33)
print(fib_num) # Цифры фибоначи

sum = 0
current_num = 0
while current_num <= 33:
    if fib_num[current_num] % 2 == 0:
        sum = sum + fib_num[current_num]
        current_num += 1
    else:
        current_num += 1

print(sum) #Правильный ответ 4 613 732

