start =int(input("enter start number: \t"))
end =int(input("enter last number: \t"))
for num in range(start,end + 1):
	if num % 2 ==0:
		print("even number",num , end = "\n ")
	else:
		print("odd number",num,end = " ")