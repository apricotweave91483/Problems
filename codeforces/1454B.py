from collections import Counter
for _ in range(int(input())):
    input()
    nums = list(map(int, input().split()))
    idx = {}
    for i in range(len(nums)):
        idx[nums[i]] = i + 1
    C = Counter(nums)
    try:
        print(idx[(sorted(x for x in C if C[x] == 1))[0]])
    except:
        print(-1)
