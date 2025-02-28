x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
OFFSET = 1000
arr = [[0 for i in range(2010)] for i in range(2010)]

for k in range(2):
    x1[k] += OFFSET
    y1[k] += OFFSET
    x2[k] += OFFSET
    y2[k] += OFFSET


for i in range(x1[0], x2[0]):
    for j in range(y1[0], y2[0]):
        arr[i][j] = 1

for i in range(x1[1], x2[1]):
    for j in range(y1[1], y2[1]):
        arr[i][j] = 0

MAX_R = 2000
min_x, max_x, min_y, max_y = MAX_R, 0, MAX_R, 0
first_rect_exist = False
for x in range(MAX_R + 1):
    for y in range(MAX_R + 1):
        if arr[x][y] == 1:
            first_rect_exist = True
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

if not first_rect_exist:
    area = 0
else:
    area = (max_x - min_x + 1) * (max_y - min_y + 1)

print(area)