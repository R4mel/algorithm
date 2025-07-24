import sys

input = sys.stdin.readline

n = int(input())

arr = map(int, list(input().rstrip()))

sum = 0
for a in arr:
    sum += a
print(sum)
