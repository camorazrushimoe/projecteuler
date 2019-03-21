#Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
#Найдите сумму всех простых чисел меньше двух миллионов.

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

prime_nums = get_primes(2000000) #this is my list of all numbers

print(len(prime_nums))
print(prime_nums[0:20])

print(prime_nums[-1])

current_num = 0
sum = 0

while current_num < 148933:
    sum = sum + prime_nums[current_num]
    current_num = current_num + 1

print(sum)