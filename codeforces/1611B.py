for _ in range(int(input())):
    a, b = map(int, input().split())
    s = 0
    if a > b:
        less = b
        more = a
    else:
        less = a
        more = b

    diff = more - less
    times = diff // 2
    if times > less:
        times = less
    less -= times
    more -= 3 * times
    s += times
    
    s += less // 2

    more -= less // 2
    less -= less // 2

    if (more == 1 and less >= 3):
        s += 1
    if (less == 1 and more >= 3):
        s += 1

    print(s)
