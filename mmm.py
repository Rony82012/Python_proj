n = int(input("Enter the len: "))
lis = [int(i) for i in input("Enter the list of integers seperated with spaces: ").split(" ")]
print(lis)

def mean (l):
	total = 0
	if len(l) < 1:
		return None
	else:
		for i in l:
			total = total + i
			mean = total / len(l)
		return mean
print("mean = %.1f" %mean(lis))


def median (l):
	lt = len(l)
	if lt < 1:
		return None
	if lt % 2 == 1:
		return sorted(l)[lt//2]
	else:
		return sum(sorted(l)[lt//2-1:lt//2+1])/2.0
print("median = ",median (lis))


def mode (l):
	m = max([l.count(a) for a in l])
	return[x for x in l if l.count(x)==m][0] if m > 1 else sorted(lis)[0]
print("mode = ", mode(lis))
