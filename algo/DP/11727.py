from sys import stdin
input = stdin.readline

n = int(input())
memo = [0]*1001


def square(n):
    if memo[n] != 0:
        return memo[n]
    else:
        if n == 1:
            memo[n] = 1
            return memo[n]
        elif n == 2:
            memo[n] = 3
            return memo[n]
        else:
            memo[n] = 2*square(n-2) + square(n-1)
            return memo[n]


print(square(n) % 10007)
