start =int(input("enter start number: \t"))
for num in range(start,start+100):
	if num > 1:
		for i in range(2,num):
			if(num % i) == 0:
				break
		else:
			print(num)