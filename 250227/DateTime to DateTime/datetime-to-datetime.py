a, b, c = map(int, input().split())

# Please write your code here.

count = 0

if a < 11:
    print(-1)
elif a == 11 and b < 11:
    print(-1)
elif a == 11 and b == 11 and c <= 11:
    print(-1)

while True:
    if a < 11:
        break
    elif a == 11 and b < 11:
        break
    elif a == 11 and b == 11 and c <= 11:
        break

    c -= 1
    count += 1

    if c == 0:
        b -= 1
        c = 60
        if b == 0:
            b = 24
            a -= 1

print(count)