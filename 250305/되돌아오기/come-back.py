def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

n = int(input())

mapper = {
    "E": 0,
    "W": 1,
    "S": 2,
    "N": 3
    # 시계방향
}

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

x = 0
y = 0
cnt = 0

for i in range(n):
    direction, dis = map(str, input().split())
    dis = int(dis)
    
    move_dir = mapper[direction]

    for _ in range(dis):
        x, y = x + dx[move_dir], y + dy[move_dir]

        cnt += 1

        if x == 0 and y == 0:
            print(cnt)
            break