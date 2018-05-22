
def linear_merge(list1,list2):
	return sorted(list1+list2)

print(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']))

'''
def remove_adjacent(nums):
	s1 = set(nums)
	return list(s1)
print(remove_adjacent([2, 2, 3, 3, 3]))
'''
'''
def last(i):
	return i[-1]
def sort_last(tuples):
	return sorted(tuples, key = last)
print(sort_last([(1, 3), (3, 2), (2, 1)]))
'''
'''
def front_x(words):
	with_x = []
	no_x =[]
	for i in words:
		if i[0] == 'x':
			with_x.append(i)
			x = sorted(with_x)
		else:
			no_x.append(i)
			y = sorted(no_x)
	return x+y
print(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))
'''
'''
def match_ends(words):
	count = 0
	for i in words:
		if len(i)>=2:
			if i[0] == i[-1]:
				count+=1
	return count


print(match_ends(['', 'x', 'xy', 'xyx', 'xx']))'''

'''def front_back(a, b):
  # +++your code here+++
  a_middle = len(a) / 2
  b_middle = len(b) / 2
  if len(a) % 2 == 1:  # add 1 if length is odd
    a_middle = a_middle + .5
  if len(b) % 2 == 1:
    b_middle = b_middle + .5
  return a[:a_middle] + b[:b_middle] + a[a_middle:] + b[b_middle:]

print(front_back('abc','xy'))'''

'''def not_bad(s):
	bad_idx = s.find("bad")
	not_idx = s.find("not")
	if not_idx > 0  and bad_idx > 0:
		if not_idx < bad_idx:
			return s[:not_idx]+'good'+s[bad_idx+3:]
		#return s
	return s

print(not_bad("This movie is not so bad maybe"))
print(not_bad("This bad movie is not hot"))
print(not_bad("This movie is bad"))'''
'''
def verbing(s):
	if len(s) < 3:
		return s
	else:
		if s[-3:] == 'ing':
			return s+"ly"
		return s+"ing"

print(verbing('cycling'))
'''

'''def donuts(count):
	#if count < 10:
	#	return print("no of d: %d", count)
	#else:
	#	return print("no on d: many")
	return print("no of donuts = ", count if count < 10 else "many")

donuts(5)
donuts(23)'''
'''
def bothends(s):
	if len(s) < 2:
		return " "
	else:
		return s[:2] + s[-2:]

print(bothends('spring'))'''

# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.
'''
def zing(s):
	x = s[0]
	y = s[1:]
	z = y.replace(x,"*")
	return x+z

print(zing("bibbow"))'''
'''
sd = "abcde"

print(sd[:2])'''
