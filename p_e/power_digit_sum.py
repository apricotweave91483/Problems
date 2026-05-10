N = 2 ** 1_000
X = 0
while N:
    X += N % 10
    N //= 10

print(X)
