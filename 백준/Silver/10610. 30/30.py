n = list(input())

while True:
    if "0" not in n:
        print(-1)
        break

    sum = 0

    for k in n:
        sum += int(k)

    if sum % 3 != 0:
        print(-1)
        break

    n.sort(reverse=True)  # 내림차순
    print(int("".join(n)))
    break
