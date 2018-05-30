#check if a given string is palindrome

def palchecker(word):
	return word == word[::-1]

def paliperm(string):
	stringlist = []
	finallist=[]
	stringlenght = len(string) - string.count(' ')
	for s in string:
		stringlist.append(s)
	dictstring = {s:stringlist.count(s) for s in stringlist}
	del dictstring[" "]
	print(dictstring)
	valueslist = [x for x in dictstring.values()]
	print(valueslist)
	if len(dictstring)%2==0 and [i%2 ==0 for i in ]

##continue later

print(paliperm('tact coa'))

'''
d = { "Hello": 2,"at" : 4,"test" : 6,"this" : 8}

print(d.items())
print(d.keys())
print(len(d))
for d in d.values():
 	print(d)

string = 'sd fa'

print(len(string) - string.count(' '))
'''