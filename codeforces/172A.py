p = []
for _ in range(int(input())):
    p.append(input())

poi = 0

while (poi < len(p[0])):
    curr = p[0][poi]
    good = 1

    for element in p[1:]:
        if element[poi] != curr:
            good = 0
            break
    if not good:
        break
    poi += 1

print(poi)

