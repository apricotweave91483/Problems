n = 0
m = 1
fib = []
while m < 4_000_000:
    temp = m
    m = n + m
    n = temp
    fib.append(m)

fib.pop()

print(sum(x for x in fib if x & 1 ^ 1))
