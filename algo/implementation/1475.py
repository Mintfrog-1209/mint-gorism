from sys import stdin
input = stdin.readline

numbers = input().rstrip('\n')
nums = [0]*10
for number in numbers:
    if number == '9':
        nums[6] += 1
    else:
        nums[int(number)] += 1

if nums[6] % 2:
    nums[6] = nums[6] // 2 + 1
else:
    nums[6] = nums[6] // 2

print(max(nums))

