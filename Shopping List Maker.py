# Objective: The aim of this assignment is to create a program that helps users make a shopping list.

#Task 1: Write a function that lets the user add items to a list.

def add_item(my_list):
    item = input("Which item would you like to add: ")
    my_list.append(item)


#Task 2: Include a function to remove items from the list.

def remove_item(my_list):
    item = input("Which item would you like to remove: ")
    if item in my_list:
        my_list.remove(item)
    else:
        print("Item is not on the list.")

#Task 3: Add a function that prints out the entire list in a formatted way.

def printed_list(my_list):
    if not my_list:
        print("The list is empty.")
    else:
        print("List contents: ")
        for i, item in enumerate(my_list):
            print(f"{i+1}. {item}")

# Not 100% sure on this one. Had to do a little research. Let me know what you think!