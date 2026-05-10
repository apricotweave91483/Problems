from sys import argv

def s(x, k):
    n = k // x
    return (n ** 2 + n) // 2 * x

N = int(argv[1]) - 1

print(s(5, N) + s(3, N) - s(15, N))
