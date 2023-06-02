def perfect_number(num):
    s = 0
    for i in range(1, num):
        if num % i == 0:
            s += i
    return num == s


for j in range(1, 10000):
    if perfect_number(j):
        print(j, end=" ")
