def is_prime(x):
    good = 1
    ub = x if x < 100 else int(x ** 0.5) + 1
    for i in range(2, ub):
        if x % i == 0:
            good = 0
            break
    return good == 1
s = 2
for x in range(3, 2_000_000, 2):
    if is_prime(x): s += x
print(s)
