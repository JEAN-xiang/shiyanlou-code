for x in range(1,100):
	if x==7:
		continue
	elif x % 7 == 0:
		continue
	elif x % 10 == 7:
		continue
	elif x // 10 == 7:
		continue
	else: 
		print(x)
		
