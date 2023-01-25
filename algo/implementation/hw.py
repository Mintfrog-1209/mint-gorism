from sys import stdin
input = stdin.readline

alpha = list(map(str, input()))
mini = list(map(str, input()))

for i in range(2):
    for j in range(len(alpha)):
        if alpha[j] == mini[i]:
            temp = alpha[j].upper
            alpha[j] = temp

for i in range(2):
    for j in range(len(alpha)):
        temp = mini[i+2].upper
        if alpha[j] == mini[i+2]:
            alpha.remove(mini[i+2])
        elif alpha[j] == temp:
            alpha.remove(temp)

for a in alpha:
    print(a, end='')
