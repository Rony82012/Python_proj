import math
pi = [float(x) for x in input('Please Enter values of type FLOAT:\n').split()]

#result = 0
def entropy(pi):
	result = 0
	for i in pi:
		summ = -i * math.log(i,2)
		result = result + summ
		#print(result)
	#print (result)
	return result

print (entropy(pi))