from sys import stdin
input = stdin.readline

height = []
for i in range(9):
    height.append(int(input()))
sum_2 = sum(height) - 100

for i in range(9):
    for j in range(9):
        if i > j:
            if len(height) != 9:
                break
            if height[i] + height[j] == sum_2:
                height.remove(height[i])
                height.remove(height[j])

height.sort()
for h in height:
    print(h)
