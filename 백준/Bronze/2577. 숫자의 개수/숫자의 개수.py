a = int(input())
b = int(input())
c = int(input())

r = str(a * b * c)

arr = [0] * 10

for i in r:
    for j in range(0, 10):
        if str(j) == i:
            arr[j] += 1

for a in arr:
    print(a)
