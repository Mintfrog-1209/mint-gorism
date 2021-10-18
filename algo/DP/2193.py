from sys import stdin
input = stdin.readline

# 1   1 0  01 10 00
# 10  0 1
# 101 100 1 1
# 1001 1010 1000 1 2
# 10101 10100 / 10010  10000 10001 2 3
# 100100 100101 / 101001 101010 101000 100001 100010 100000 3 5
# 5 8
# 끝자리 1 * 2 끝자리 0 * 3
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
