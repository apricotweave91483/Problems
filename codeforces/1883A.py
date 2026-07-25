def do(x):
    x = list(map(int, (c for c in x)))
    for i in range(len(x)):
        if x[i] == 0:
            x[i] = 10
    x = [1] + x
    su = 4
    for i in range(len(x) - 1):
        su += abs(x[i] - x[i + 1])

    print(su)

for _ in range(int(input())):
    do(input())
