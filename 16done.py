i = 2**1000

print(i)
i = str(i)
print(len(i))
print(i[0:10])

def in_int(n):
    n = int(n)
    return n

def in_str(h):
    h = str(h)
    return h


#302
v = len(i) - 1
sum = 1
line_num = 0
print(i[line_num + 1])

while line_num < v:
    sum = sum + in_int(i[line_num + 1])
    line_num = line_num + 1
    print(sum)
