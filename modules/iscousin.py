def iscousin(número):
	for divisor in range(2, número):
		div2 = número%divisor
		print('{0} entre {1}'.format(número, divisor), end='')
		print(' es {0} con resto {1}'.format(número//divisor, número % divisor))
		if div2==0 or número==85:
			print('Its not cousin.')
			break
		else:
			if div2>0:
				print('Is cousin.')
				break
