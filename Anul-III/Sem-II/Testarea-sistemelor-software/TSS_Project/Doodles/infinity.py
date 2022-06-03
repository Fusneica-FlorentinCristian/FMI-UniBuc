import math


def area_sums(r, a, b):
    sum_aria = 0
    cnt = 1
    while r >= 1.0:
        if cnt == 2:
            r *= float(a)
        elif cnt == 3:
            r = int(r / b)
            cnt = 1
        if r == 0:
            break
        cnt += 1
        sum_aria += math.pi * int(r) ** 2
    return sum_aria


with open("input.in", "r") as f:
    n = int(f.readline())
    list_sums = [area_sums(*[float(elem) for elem in f.readline().split(" ")]) for _ in range(n)]

    for (index, elem) in enumerate(list_sums):
        print(f"Case #{index + 1}: {round(elem, 6)}")
