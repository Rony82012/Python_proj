''' given a list for ex: [1,7,5,9,2,12,3], give the count,
 where the pair difference is two '''

def difftwo (list1):
	list1 = sorted(list1)
	count = 0 
	for i in range(len(list1)-1):
		for j in range(1, len(list1)):
			if list1[j] - list1[i] == 2:
				count+=1
	print(count)


	#print(list1[j], list1[i])


difftwo([1,7,5,9,2,12,3])