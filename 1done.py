list = [1, 2, 3]
a = 4

while a < 1000:
    a += 1
    list.append(a)

print(list)
print(list[998])

list_number = 0
sum = 0

print(list[list_number])

while list_number <= 999:
    if list_number % 3 == 0 or list_number % 5 == 0:
        sum = sum + list_number
        list_number += 1
    else:
        list_number += 1

print(sum)


