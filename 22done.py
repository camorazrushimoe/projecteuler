'''
Используйте names.txt (щелкнуть правой кнопкой мыши и выбрать 'Save Link/Target As...'),
текстовый файл размером 46 КБ, содержащий более пяти тысяч имен. Начните с сортировки в
алфавитном порядке. Затем подсчитайте алфавитные значения каждого имени и умножьте
это значение на порядковый номер имени в отсортированном списке для получения
количества очков имени.

Например, если список отсортирован по алфавиту, имя COLIN (алфавитное значение
которого 3 + 15 + 12 + 9 + 14 = 53) является 938-ым в списке. Поэтому,
имя COLIN получает 938 × 53 = 49714 очков.

Какова сумма очков имен в файле?
'''

def alphabet_sum(name):
    sum = 0
    actual_num = 0
    max_num = len(name)
    while actual_num < max_num:
        int(alphabet.index(name[actual_num]))
        sum = sum + alphabet.index(name[actual_num]) + 1
        actual_num = actual_num + 1
    return int(sum)


alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
txt = open("files/p022_names.txt", "r")
#print(names.read())
names = txt.read().split("\",\"")
print(names)
del(names[0])
names.insert(0, "MARY")
del(names[-1])
names.append("ALONSO")
print(names)
print("Alphabet power of MARY: ", alphabet_sum(names[0]))

names = sorted(names) # sort list
print(names)

max_len = len(names) # 5163 size of the list
test = []
current_pos = 0

while current_pos < 5163:
    test.insert(current_pos+1, alphabet_sum(names[current_pos]) * (current_pos + 1))
    current_pos = current_pos + 1

print(names)
print(test)

q = 0
qq = 0 # sum of all numbers in new list
while q < 5163:
    qq = qq + test[q]
    q = q + 1
print("Answer is: ", qq)