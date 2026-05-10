n = 1

from math import lcm

for x in range(2, 21):
    n = lcm(x, n)

print(n)
