import sys

input = sys.stdin.readline

s = list(input())

arr = [0] * 26

for i in range(len(s)):
    for j in range(len(arr)):
        if ord(s[i]) == ord("a") + j:
            arr[j] += 1
            break

for a in arr:
    print(a, end=" ")
