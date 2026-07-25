for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print((abs(a - b) + abs(a - c) + abs(b - c))//2)
