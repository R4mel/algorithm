import sys

input = sys.stdin.readline

text = input().rstrip()

for i in range(0, len(text), 10):
    print(text[i : i + 10])
