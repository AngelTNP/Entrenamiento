def __main__():

	max = 0
	num = 1
	for x in range(1,1000001):
		step = 1
		n = x
		while(n!=1):
			if(n%2==0):
				n/=2
			else:
				n=3*n+1
			step+=1
		if(max<step):
			max = step
			num = x
	print(num, max)

__main__()