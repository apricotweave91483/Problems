def check(arr) -> int:
    return sum(1 for i in range(len(arr) - 2) if arr[i] + arr[i + 1] == arr[i + 2])
for _ in range(int(input())):
    x0, x1, x2, x3 = map(int, input().split())
    A1 = x0 + x1
    A2 = x2 - x1
    
    n1 = [x0, x1, A1, x2, x3]
    n2 = [x0, x1, A2, x2, x3]
    print(max(check(n1), check(n2)))

