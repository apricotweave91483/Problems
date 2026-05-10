def pal(n):
    return str(n) == str(n)[::-1]

mx = -1

dig = 3
lb = 10 ** (dig - 1)
ub = 10 ** dig

for x in range(lb, ub):
    for y in range(x + 1, ub):
        if pal(x * y):
            mx = max(x * y, mx)

print(mx)

