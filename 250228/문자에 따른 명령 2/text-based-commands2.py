dirs = list(input())

# Please write your code here.
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

x, y = 0, 0
dir_num = 3 #북쪽

for i in range(len(dirs)):
    if dirs[i] == "L":
        dir_num = (dir_num + 3) % 4
    elif dirs[i] == "R":
        dir_num = (dir_num + 1) % 4
    elif dirs[i] == "F":
        x = x + dx[dir_num]
        y = y + dy[dir_num]

print(x, y)

# 직진 F
# x = x + dx[dir_num]
# y = y + dy[dir_num]

# 우회전 R
# dir_num = (dir_num + 1) % 4

# 좌회전 L
# dir_num = (dir_num + 3) % 4

# 뒤돌기
# dir_num = (dir_num + 2) % 4

# arr = [1,2,3,0]
# dir_num = arr[dir_num]

# if dir_num == 0:
#     dir_num = arr[dir_num]
# elif dir_num == 1:
#     dir_num = arr[dir_num]
# elif dir_num == 2:
#     dir_num = arr[dir_num]
# elif dir_num == 3:
#     dir_num = arr[dir_num]
