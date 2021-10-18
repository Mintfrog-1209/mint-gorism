from sys import stdin
input = stdin.readline

memo = [0]*101


def halfwave(n):
    if memo[n] != 0:
        return memo[n]
    else:
        if n == 1 or n == 2 or n == 3:
            memo[n] = 1
            return memo[n]
        elif n == 4 or n == 5:
            memo[n] = 2
            return memo[n]
        else:
            memo[n] = halfwave(n-5) + halfwave(n-1)
            return memo[n]


t = int(input())

for i in range(t):
    n = int(input())
    print(halfwave(n))
