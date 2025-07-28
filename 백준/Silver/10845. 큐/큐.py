import sys
from collections import deque

input = sys.stdin.readline

queue = deque()

n = int(input())
for _ in range(n):
    tmp = list(input().split())
    if tmp[0] == "push":
        queue.append(int(tmp[1]))
    if tmp[0] == "pop":
        print(queue.popleft() if len(queue) != 0 else -1)
    if tmp[0] == "size":
        print(len(queue))
    if tmp[0] == "empty":
        print(1 if len(queue) == 0 else 0)
    if tmp[0] == "front":
        print(queue[0] if len(queue) != 0 else -1)
    if tmp[0] == "back":
        print(queue[-1] if len(queue) != 0 else -1)
