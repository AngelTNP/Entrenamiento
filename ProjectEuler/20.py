def factorial(x):
	if(x<=1):
		return 1
	else:
		return x*factorial(x-1)

def __main__():
	fac = str(factorial(100))
	sum = 0
	for x in fac:
		sum+=int(x)
	print(sum)


__main__()