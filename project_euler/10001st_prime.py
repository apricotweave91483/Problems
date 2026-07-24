def is_prime(x):
    good = 1
    for i in range(2, x):
        if x % i == 0:
            good = 0
            break
    return good == 1


start = 2
primes = [start]

while len(primes) != 10_001:
    start += 1
    if is_prime(start):
        primes.append(start)

print(start, len(primes))

    
