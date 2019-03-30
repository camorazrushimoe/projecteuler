'''
Дана следующая информация (однако, вы можете проверить ее самостоятельно):

1 января 1900 года - понедельник.
В апреле, июне, сентябре и ноябре 30 дней.
В феврале 28 дней, в високосный год - 29.
В остальных месяцах по 31 дню.
Високосный год - любой год, делящийся нацело на 4, однако последний год века (ХХ00)
является високосным в том и только том случае, если делится на 400.
Сколько воскресений выпадает на первое число месяца в двадцатом веке
(с 1 января 1901 года до 31 декабря 2000 года)?
'''

# прогнать все первые числа каждого месяца, каждого года и складывать в массив если это воскресенье

from datetime import date
import calendar

year = 1901
mounth = 1
day = 1

my_date = date(year, mounth, day)

print(calendar.day_name[my_date.weekday()])  #show day name
sum_of_sundays = 0
year = 1901

while year < 2001:
    mounth = 1
    day = 1
    while mounth < 13:
        my_date = date(year, mounth, day)
        if calendar.day_name[my_date.weekday()] != "Sunday":
            mounth += 1
        else:
            sum_of_sundays += 1
            print(mounth)
            mounth += 1
    year += 1

print(sum_of_sundays)

