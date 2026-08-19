for _ in range(int(input())):
    n = int(input())
    rows = [(['.'] * (2 * n))[:] for i in range(2 * n)]
    for row in range(2 * n):
        for col in range(2 * n):
            if not ((row // 2) & 1 ^ 1) ^ ((col // 2) & 1 ^ 1):
                rows[row][col] = '#'
    for row in rows:
        print("".join(row))
