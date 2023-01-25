from sys import stdin
input = stdin.readline

num = input().rstrip()
answer = int(num[0])
for n in range(1, len(num)):
    if int(num[n]) == 0 or int(num[n]) == 1 or answer == 0:
        answer += int(num[n])
    else:
        answer *= int(num[n])

print(answer)
