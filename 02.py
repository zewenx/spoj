import math


def print_list(s):
    for x in s:
        print(x)


def find_prime(aa, b, current):
    target = []
    for x in range(aa, b+1):
        if x == 1:
            x += 1
            continue
        if is_prime(x, current):
            target.append(x)
        x += 1
    return target


def is_prime(x, current):
    for t in range(2, int(math.sqrt(x))+1):
        if x % t == 0:
            return False
    return True


a = input()
a = int(a)
while a > 0:
    strs = input()

    target = find_prime(int(strs.split(" ")[0]), int(strs.split(" ")[1]))
    a -= 1