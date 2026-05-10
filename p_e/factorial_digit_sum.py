from math import factorial as f

n = f(100)

x = 0
while n:
    x += n % 10
    n //= 10

print(x)
