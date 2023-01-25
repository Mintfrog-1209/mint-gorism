# 1009 각 자리수의 역과 합

from sys import stdin
input = stdin.readline

while True:
    nums = input().rstrip()
    start = False
    if nums == '0':
        break
    else:
        arr = []
        for num in nums:
            arr.append(int(num))
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == 0 and not start:
                pass
            else:
                print(arr[i], end='')
                start = True
        print('', end=' ')
        print(sum(arr))