for _ in range(int(input())):
    input()
    First = list(map(int, input().split()))

    Nums = []
    for num in First:
        if num % 6 == 0:
            Nums.append(num)
    
    for num in First:
        if num % 6:
            Nums.append(num)

    new = []
    for num in Nums:
        if num & 1 ^ 1:
            new.append(num)
    for num in Nums:
        if num % 3 != 0 and num & 1:
            new.append(num)
    for num in Nums:
        if num % 3 == 0 and num & 1:
            new.append(num)

    print(" ".join(str(x) for x in new))


