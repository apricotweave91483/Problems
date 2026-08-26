n = int(input())
s = input()

diff = 1

poi = 0

tot = []

while 1:
    try:
        tot.append(s[poi])
    except:
        print("".join(tot))
        exit(0)
    poi += diff
    diff += 1


