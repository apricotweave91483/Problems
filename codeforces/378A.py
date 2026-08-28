di = [1, 2, 3, 4, 5, 6]

a, b = map(int, input().split())

ans = [0, 0, 0]

for d in di:
    if abs(a - d) < abs(b - d):
        ans[0] += 1
    elif abs(a - d) > abs(b - d):
        ans[-1] += 1
    else:
        ans[1] += 1

print(" ".join(str(x) for x in ans))
