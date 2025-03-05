x, y = 0, 0

mapper = {
    'F': 0,
    'L': 1,
    'R': 2
}

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

a = list(input())

dir_num = 0

answer = -1
time = 0

for i in range(len(a)):
    if a[i] == 'L':
        dir_num = (dir_num + 3) % 4
        time += 1
    elif a[i] == 'R':
        dir_num = (dir_num + 1) % 4
        time += 1
    elif a[i] == 'F':
        x = x + dx[dir_num]
        y = y + dy[dir_num]
        time += 1

    if x == 0 and y == 0:
        answer = time
        break

print(answer)