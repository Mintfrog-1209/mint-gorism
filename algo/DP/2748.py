from sys import stdin
input = stdin.readline

memo = [0]*100


def fibo(n):
    if memo[n] == 0:
        if n == 1:
            return 1
        elif n == 0:
            return 0
        else:
            memo[n] = fibo(n-1) + fibo(n-2)
            return memo[n]
    else:
        return memo[n]


n = int(input())
print(fibo(n))
