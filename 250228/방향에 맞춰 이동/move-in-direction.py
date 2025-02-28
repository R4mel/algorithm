N = int(input())

cur_x, cur_y = 0, 0

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(N):
    dir_c, dist = map(str, input().split())
    dist = int(dist)

    if dir_c == 'E':
        dir_num = 0
    elif dir_c == 'S':
        dir_num = 1
    elif dir_c == 'W':
        dir_num = 2
    else:
        dir_num = 3

    cur_x = cur_x + dx[dir_num] * dist
    cur_y = cur_y + dy[dir_num] * dist

print(cur_x, cur_y)

# x,y = map(int, input().split())
# dir_num = int(input())

# dx = [1, 0, -1, 0]
# dy = [0, -1, 0, 1]

# x = x + dx[dir_num]
# y = y + dy[dir_num]

# print(x, y)