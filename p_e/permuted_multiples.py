x = 1
def cond(x):
    return set(str(x * 6)) == set(str(x * 5)) and set(str(x * 5)) == set(str(x * 4)) and set(str(x * 4)) == set(str(x * 3)) and set(str(x * 3)) == set(str(x * 2)) and set(str(x * 2)) == set(str(x))

while not cond(x):
    x += 1

print(x)
