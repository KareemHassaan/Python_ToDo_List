ToDoList = list()
DoneList = []

def AddToDoList():
	#scanning the number of items from user
	number = int(input("Enter how many item you want : "))
	
	#scanning the items from user
	for item in range(0,number):
		
		element = str(input("Enter item " + str(item + 1) + " : "))
		ToDoList.append(element)
	
	#printing the new to do list
	print("you have now " + str(len(ToDoList)) + " items in the To Do List : ")		
	print(ToDoList)
	print("\n")
		
def RemoveToDoList():
	#scanning the number of items from user
	number = int(input("Enter how many item you want to remove : "))
	
	#scanning the items from user to remove
	for item in range(0,number):
		
		element = str(input("Enter item " + str(item + 1) + " to remove : "))
		ToDoList.remove(element)
	
	#printing the new to do list
	print("you have now " + str(len(ToDoList)) + " items in the To Do List : ")	
	print(ToDoList)
	print("\n")	
		
def PrintToDoList():
	#printing the to do list
	print("you have now " + str(len(ToDoList)) + " items in the To Do List : ")
	print(ToDoList)
	print("\n")
		
def MoveDoneList():
	#scanning the number of items from user
	number = int(input("Enter how many item you want to move to Done list : "))
	
	#scanning the items from user to move to Done list
	for item in range(0,number):
		
		element = str(input("Enter item " + str(item + 1) + " to move to Done list : "))
		ToDoList.remove(element)
		DoneList.append(element)
	
	#printing the new Done list
	print("you have now " + str(len(ToDoList)) + " items in the Done List : ")	
	print(DoneList)
	print("\n")	
	
def PrintDoneList():
	#printing the Done list
	print("you have now " + str(len(ToDoList)) + " items in the Done List : ")
	print(DoneList)
	print("\n")