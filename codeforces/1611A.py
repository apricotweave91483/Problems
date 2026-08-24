for _ in range(int(input())):
    s = input()
    if int(s[-1]) & 1 ^ 1:
        print(0)
        continue

    if int(s[0]) & 1 ^ 1:
        print(1)
        continue
    
    good = 0
    for x in s[1:-1]:
        if int(x) & 1 ^ 1:
            good = 1
            print(2)
            break
    if good:
        continue

    print(-1)
    


