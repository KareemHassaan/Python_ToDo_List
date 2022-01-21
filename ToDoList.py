import ListOperations
from ListOperations import AddToDoList,RemoveToDoList,PrintToDoList,MoveDoneList,PrintDoneList

while(1):
	#Scanning from the user the operation that he want
	operation = int(input('''	|******************** To Do List ********************|
	|Enter (1) to Add item to the to do list             |
	|Enter (2) to Remove item from to do list            |
	|Enter (3) to Print the to do list                   |
	|Enter (4) to Move item to done list                 |
	|Enter (5) to Print done list                        |
	|****************************************************|\n'''))

	if operation == 1:
		AddToDoList()
		
	elif operation == 2:
		RemoveToDoList()
			
	elif operation == 3:
		PrintToDoList()

	elif operation == 4:
		MoveDoneList()
	
	elif operation == 5:
		PrintDoneList()

	else :
		print("Sorry this option is unavailable")