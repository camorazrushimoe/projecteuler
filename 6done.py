#Сумма квадратов первых десяти натуральных чисел равна
#12 + 22 + ... + 102 = 385
#Квадрат суммы первых десяти натуральных чисел равен
#(1 + 2 + ... + 10)2 = 552 = 3025
#Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных чисел составляет 3025 − 385 = 2640.
#Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.


squares_of_sum = 1

list = []
a = 1
sum_of_sq = 0
current_num = 0

while a < 101:
    list.append(a)
    a = a + 1

while current_num < 100:
    sum_of_sq = sum_of_sq + list[current_num] * list[current_num]
    current_num = current_num + 1

print(list)
print(sum_of_sq)

list = []
a = 1
sq_of_sum = 0
current_num = 0

while a < 101:
    list.append(a)
    a = a + 1

while current_num < 99:
    sq_of_sum = sq_of_sum + list[current_num] + list[current_num+1]
    current_num = current_num + 2

print(list)
print(sq_of_sum)
print(sq_of_sum*sq_of_sum)

print(sq_of_sum * sq_of_sum - sum_of_sq) # ответ 25164150