def reverse(x):
	if x < 0:
		return -reverse(-x)
	sol = 0
	while x:
		sol = x %10 + sol *10
		x = x // 10
	if sol > 2147483647:
		return 0
	return sol

#print(reverse(-123))
