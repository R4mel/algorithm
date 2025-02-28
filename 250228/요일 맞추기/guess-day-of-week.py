m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
total_days1 = 0
total_days2 = 0

# 1/1부터 m1, d1까지 날짜
for i in range(1, m1):
    total_days1 += num_of_days[i]

total_days1 += d1

# 1/1부터 m2, d2까지 날짜
for i in range(1, m2):
    total_days2 += num_of_days[i]

total_days2 += d2

diff = total_days2 - total_days1
while diff < 0:
    diff += 7

day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(day_of_week[diff % 7])