def factorial(x):
	if(x<=1):
		return 1
	else:
		return x*factorial(x-1)

def __main__():
	tam = 20
	routes = factorial(2*tam)/(factorial(tam)**2)
	print(routes)

__main__()