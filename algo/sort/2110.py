#2110 공유기 설치

from sys import stdin
input = stdin.readline

n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()


def condition(distance):
    dist = 0
    router = c-1
    for h in range(1, n):
        dist += house[h] - house[h-1]
        if dist >= distance :
            router -= 1
            dist = 0
    if router > 0:
        return False
    else:
        return True

def bsearch(n):
    start = 0
    end = n
    while start + 1 < end :
        mid = (start + end) // 2
        if condition(mid):
            start = mid
        else:
            end = mid
    if condition(mid):
        return mid
    else:
        return mid-1
print(bsearch(house[n-1]))
        


