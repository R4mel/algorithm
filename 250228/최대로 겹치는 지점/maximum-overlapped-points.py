N = int(input())

# Please write your code here.

arr = [0 for i in range(110)]

for _ in range(N):
    segments = tuple(map(int, input().split()))
    for i in range(segments[0], segments[1] + 1):
        arr[i] += 1

print(max(arr))        
