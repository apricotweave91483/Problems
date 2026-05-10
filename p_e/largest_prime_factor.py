from sys import argv

primes = []

for x in range(2, 10_000):
    good = 1
    for i in range(2, x):
        if x % i == 0:
            good = 0
            break
    if good:
        primes.append(x)

mx = -1

for prime in primes:
    if int(argv[1]) % prime == 0:
        mx = prime
print(mx)

