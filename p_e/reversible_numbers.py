def good(x):
    strx = str(x)
    if strx[-1] == "0":
        return False
    x += int(strx[::-1])
    while x:
        if x % 10 & 1 ^ 1:
            return False
        x //= 10
    return True

print(sum(1 for x in range(1, 10 ** 9) if good(x)))
