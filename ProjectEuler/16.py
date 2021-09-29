def __main__():
	x = str(2**1000)
	sum = 0
	for y in x:
		sum+=int(y)
	print(sum)

__main__()