n = int(input())
nums = list(map(int, input().split()))

new = []

for i in range(n - 1):
    new.append(nums[i] + nums[i + 1])
new.append(nums[-1])

print(" ".join(str(x) for x in new))

