def s(n):
	return sum(int(c) for c in str(n))

mx = -1
for a in range(1, 100):
	for b in range(1, 100):
		x = a ** b
		mx = max(mx, s(x))
print(mx)
