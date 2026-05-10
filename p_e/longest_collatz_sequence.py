def do_it(n):
    cnt = 1
    while n ^ 1:
        n = 3 * n + 1 if n & 1 else n // 2
        cnt += 1
    return cnt

mx = -1
best = None

for x in range(1, 1_000_000):
    y = do_it(x)
    if y > mx:
        best = x
        mx = y

print(best)

