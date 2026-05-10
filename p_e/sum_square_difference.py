def s1(n):
    return ((n ** 2 + n) // 2) ** 2
def s2(n):
    return n * (n + 1) * (2 * n + 1) // 6

from sys import argv
N = int(argv[1])

print(s1(N) - s2(N))
