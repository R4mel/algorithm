n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
# x = [0, 4, 0]
# y = [0, 0, 4]
OFFSET = 100
arr = [[0 for i in range(210)] for i in range(210)]

for i in range(n):
    x[i] += OFFSET
    y[i] += OFFSET
    for j in range(x[i], x[i] + 8):
        for k in range(y[i], y[i] + 8):
            arr[j][k] = 1

cnt = 0
for i in range(210):
    for j in range(210):
        if arr[i][j] == 1:
            cnt += 1

print(cnt)



