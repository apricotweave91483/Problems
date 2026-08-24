for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    nums.sort(key=lambda x: x * -1)

    tot = 0

    for i in range(n):
        tot += max(nums[:i + 1])

    print(tot)

