
for _ in range(int(input())):
    n = int(input())
    for x in list(map(int, input().split())):
        print(n - x + 1, end=" ")
    print()
    
