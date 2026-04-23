numbers = []

while True:
	print("1. Add")
	print("2. Remove")
	print("3. Display")
	print("4. Quit")
	choice = input("Enter choice: ")

	# ADD
	if choice == "1":
		num = int(input("Integer: "))
		numbers.append(num)
		print("List after adding:",numbers)
	# REMOVE
	elif choice == "2":
		if not numbers:
			print("List is empty")
		else:
			num = int(input("Integer: "))
			if num in numbers:
				numbers.remove(num)
				print("List after removing:", numbers)
			else:
				print("Element not found")
	# DISPLAY
	elif choice == "3":
		if not numbers:
			print("List is empty")
		else:print(numbers)
	# QUIT 
	elif choice == "4":
		break
	# INVALID MENU OPTION
	else:
		print("Invalid choice")
