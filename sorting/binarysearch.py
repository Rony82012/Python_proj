def binarysearch(alist, num):
	if len(alist) == 0:
		return False
	else:
		midpoint = len(alist)//2
		if alist[midpoint] == num:
			return True
		else:
			if num<alist[midpoint]:
				return binarysearch(alist[:midpoint],num)
			else:
				return binarysearch(alist[midpoint+1:],num)


testlist = [90, 11, 32, 28, 13, 47, 19, 2, 22,]
print(binarysearch(sorted(testlist), 3))
print(binarysearch(sorted(testlist), 13))