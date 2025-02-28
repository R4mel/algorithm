'''

arr[위에서 몇번째][왼쪽에서 몇번째]

arr[행][열]

arr[x][y]

arr[x + 1][y] -> 아래
arr[x][y + 1] -> 오른쪽

'''

N = int(input())

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

arr = [list(map(int, input().split())) for i in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

answer = 0

for x in range(N):
    for y in range(N):
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not in_range(nx, ny):
                continue

            if arr[nx][ny] == 1:
                cnt += 1
            
        if cnt >= 3:
            answer += 1
print(answer)

# total = 0
# for i in range(4):
#     nx = x + dx[i]
#     ny = y + dy[i]

#     if not in_range(nx, ny):
#         continue
    
#     total += arr[nx][ny]

# print(total)