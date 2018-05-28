'''given a smaller string 's' and a bigger string 'b', find all the 
permutations of 's' within 'b'''

s = 'abbc'
b = 'cbabadcbbabbcbabaabccbabc'

def stringperm (s,b):
	count = 0
	for i in range(len(b)-3):
	#print(b[i:i+2])
		if b[i:i+4] == s:
			#print('found')
			count+=1
	return count

print(stringperm(s,b))