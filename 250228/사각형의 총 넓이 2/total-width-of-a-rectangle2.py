N = int(input())

h = [[0 for i in range(210)] for i in range(210)]

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            h[x][y] = 1

cnt = 0
for i in range(210):
    for j in range(210):
        if h[i][j] == 1:
            cnt += 1

print(cnt)