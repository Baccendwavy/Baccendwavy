# [ ] create, call and test the adding_report() function

def adding_report (report):
	
	total = 0 
	items  = ""
	
	print('Input an integer to add to the total or "Q" to quit:')
	
	# running infinite while loop
	while True:
		# taking input
		inp = input('Enter an integer or "Q"): ')
		
		# checking if input is integer
		if inp.isdigit():
			total += int(inp)
			items += inp + "\n"
		
		# else checking if first letter is Q
		elif inp[0].upper() == "Q":
			# printing report based on given parameter
			if report == "T":
				print("\nTotal\n "+str(total))
			
			elif report == "A":
				print("\nItems")
				print(items)
				print("Total\n "+str(total))
				
			break
		
		# printing invalid input	
		else:
			print(inp+" is invalid input")