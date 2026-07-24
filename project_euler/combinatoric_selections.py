from math import comb

x = 0
for n in range(1, 100 + 1):
    for r in range(1, n):
        if comb(n, r) > 1_000_000:
            x += 1
print(x)
