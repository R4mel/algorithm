x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
arr = [[0 for i in range(2010)] for i in range(2010)]

for i in range(2):
    for x in range(x1[i], x2[i]): # 1 ~ 3
        for y in range(y1[i], y2[i]): # 2 ~ 5
            arr[x][y] = 1

for x in range(x1[2], x2[2]):
    for y in range(y1[2], y2[2]):
        arr[x][y] = 0

cnt = 0
for i in range(2010):
    for j in range(2010):
       if arr[i][j] == 1:
        cnt += 1

print(cnt) 
            

