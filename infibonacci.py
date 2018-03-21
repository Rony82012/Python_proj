def fibonacci(n):
	current = 0
	after = 1
	for i in range(n):
		current,after = after, current+after
		
		print (current)
	return None



fibonacci(694539)