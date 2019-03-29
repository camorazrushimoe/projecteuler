'''
Если записать числа от 1 до 5 английскими словами (one, two, three, four, five),
то используется всего 3 + 3 + 5 + 4 + 4 = 19 букв.

Сколько букв понадобится для записи всех чисел от 1 до 1000 (one thousand) включительно?

Примечание: Не считайте пробелы и дефисы. Например, число 342
(three hundred and forty-two) состоит из 23 букв, число 115
(one hundred and fifteen) - из 20 букв. Использование "and"
при записи чисел соответствует правилам британского английского.
'''

import inflect

p = inflect.engine()
print(p.number_to_words(99))


my_list = []
i = 1

while i != 1001:
    my_list.append(i)
    i += 1

print("list of all nums: ", my_list)

list_with_text_num = []
i = 0

while i < 1000:
    list_with_text_num.append(p.number_to_words(my_list[i]))
    i += 1

print("list of all nums in words style: ", list_with_text_num)

# def del_all_symbol(n)
#     n

def del_symbols(n): #function, they can delet "-" and " " from the string
    n = n.replace(" ", "")
    n = n.replace("-", "")
    return n

#206
#222

# print(del_symbols(list_with_text_num[20]))
# print(del_symbols(list_with_text_num[222]))
# print(del_symbols(list_with_text_num[206]))

i = 0
final_v = ""

while i < 1000:
    #final_list.append(del_symbols(list_with_text_num[i]))
    final_v = final_v + del_symbols(list_with_text_num[i])
    i += 1

print(final_v)
print("Answer is: ", len(final_v))
