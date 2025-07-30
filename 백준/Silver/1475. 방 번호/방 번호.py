import math

n = list(input())

a = [0] * 10

for i in n:
    a[int(i)] += 1

a[6] = (a[6] + a[9] + 1) // 2
a[9] = a[6]

print(max(a))
