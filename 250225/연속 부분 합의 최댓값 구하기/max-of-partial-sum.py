import sys

INT_MIN = -sys.maxsize

n = int(input())
arr = list(map(int, input().split()))

arr.insert(0,0)

# Write your code here!
# dp[1] = max(dp[0] + a[1], 2a[1])
# dp[1] = max(6, -4) -> 6

# dp[i] = max(dp[i-1] + a[i], a[i])

dp = [0] * (n+1)

def initialize():
    for i in range(1, n+1):
        dp[i] = INT_MIN
    dp[1] = 2 * arr[1]

initialize()

for i in range(2, n+1):
    dp[i] = max(dp[i-1]+ arr[i], arr[i])

ans = INT_MIN
for i in range(1, n+1):
    ans = max(ans , dp[i])

print(ans)