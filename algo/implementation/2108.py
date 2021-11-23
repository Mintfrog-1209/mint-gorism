# 2108 통계학
from sys import stdin
input = stdin.readline

n = int(input())
num = []
for i in range(n):
    num.append(int(input()))
num.sort()
mean = round(sum(num) / n)
med = num[n//2]


def most():
    times = [0]*8001
    for i in range(n):
        indx = num[i] + 4000
        times[indx] += 1
    first_max = times.index(max(times))
    times[first_max] += -1
    second_max = times.index(max(times))
    if times[first_max] + 1 == times[second_max]:
        return second_max - 4000
    else:
        return first_max - 4000


mosts = most()
rng = num[-1] - num[0]

print(mean)
print(med)
print(mosts)
print(rng)
