x = 1
y = 1
 
fib = set()
 
while (x + y) <= 1000:
	prev = x
	x = x + y
	y = prev
	fib.add(y)
 
fib.add(x)
 
s = []
 
for i in range(1, int(input()) + 1):
	if i in fib:
		s.append("O")
		continue
	s.append("o")
 
print("".join(s))
