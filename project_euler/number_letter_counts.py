tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}

teens = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}

dig = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

def numstr(x):
    if x == 1000:
        return "onethousand"

    s = ""
    if x >= 100:
        s += dig[x // 100] + "hundred"
        if x % 100:
            s += "and"
            n = x % 100
            if n < 10:
                s += dig[n]
            elif n >= 10 and n < 20:
                s += teens[n]
            elif n >= 20:
                s += tens[n // 10]
                if n % 10:
                    s += dig[n % 10]
    elif x >= 10 and x < 20:
        s += teens[x]
    elif x < 10:
        s += dig[x]
    elif x >= 20:
        s += tens[x // 10]
        if x % 10:
            s += dig[x % 10]
    return s

from sys import argv

total = ""

if len(argv) > 1:
    print(numstr(int(argv[1])))
    exit(0)

for x in range(1, 1001):
    total += numstr(x)

print(len(total))
