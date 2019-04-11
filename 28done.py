'''
http://euler.jakumo.org/problems/view/28.html

Начиная с числа 1 и двигаясь дальше вправо по часовой стрелке, образуется следующая спираль 5 на 5:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

73 74 75 76 77 78 79 80 81
72 43 44 45 46 47 48 49 50
71 42 21 22 23 24 25 26 51
70 41 20  7  8  9 10 27 52
69 40 19  6  1  2 11 28 53
68 39 18  5  4  3 12 29 54
67 38 17 16 15 14 13 30 55
66 37 36 35 34 33 32 31 56
65 64 63 62 61 60 59 58 57

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
Можно убедиться, что сумма чисел в диагоналях равна 101.

Какова сумма чисел в диагоналях спирали 1001 на 1001, образованной таким же способом?
'''

#print(21+7+1+3+12+25+9+5+17+1)

right_top = 1
i = 2
sum = 1
row_count = 1

#while right_top < 100:
while row_count < 1001:
    right_top = right_top + (4 * i)
    left_top = right_top - i
    left_bottom = left_top - i
    right_bottom = left_bottom - i
    i = i + 2
    row_count = i - 1
    print("len of YxY is: ", row_count)
    print("left_top is: ", left_top, "right_top is: ", right_top, "left_buttom is: ", left_bottom, "right_bottom is: ", right_bottom)
    sum = sum + right_top + right_bottom + left_bottom + left_top
    print(sum)

print("Answer is ", sum) # 669171001