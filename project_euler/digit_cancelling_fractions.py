def valid(x, y):
    xstr = str(x)
    ystr = str(y)

    common = None

    for char in xstr:
        if char in ystr:
            common = char

    if common is None or common == "0":
        return False
    
    xstr = xstr.replace(common, "")
    ystr = ystr.replace(common, "")

    if xstr == "":
        xstr = common
    if ystr == "":
        ystr = common
    if int(ystr) == 0:
        return False

    return (x / y) == (int(xstr) / int(ystr))
numerator = 1
denominator = 1
for x in range(10, 100):
    for y in range(x + 1, 100):
        if valid(x, y):
            numerator *= x
            denominator *= y

print(numerator, "/", denominator)
print(denominator / numerator)

