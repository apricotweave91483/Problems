from collections import Counter
dig = []
input()
cnt = Counter(input())
while (cnt['n'] > 0):
    dig.append('1')
    cnt['n'] -= 1
    cnt['o'] -= 1
    cnt['e'] -= 1
dig.extend(['0'] * cnt['z'])
print(" ".join(dig))

