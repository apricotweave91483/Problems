with open("names.txt", "r") as f:
    contents = f.read()

names = (contents.replace('"', '')).split(",")

names.sort()

def worth(name):
    s = 0
    for char in name:
        n = ord(char) - ord("A")
        n += 1
        s += n
    return s

ans = 0

for x in range(len(names)):
    name = names[x]
    place = x + 1
    ans += place * worth(name)

print(ans)

