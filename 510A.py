x, y = map(int, input().split())

rows = [(['.'] * y)[:] for i in range(x)]

for i in range(x):
    if i & 1 ^ 1:
        rows[i] = ['#'] * y
    elif i // 2 & 1 ^ 1:
        rows[i][-1] = '#'
    else:
        rows[i][0] = '#'


for row in rows:
    print("".join(row))
