# Objective: The aim of this assignment is to create a program that helps users make a shopping list.



def add_item(my_list, item):
    item = input("Which item would you like to add: ")
    my_list.append(item)

def remove_item(my_list, item):
    item = input("Which item would you like to remove: ")
    if item in my_list:
        my_list.remove(item)
    else:
        print("Item is not on the list.")

def printed_list(my_list, item):
    if not my_list:
        print("The list is empty.")
    else:
        print("List contents: ")
        for i, item in enumerate(my_list):
            print(f"{i+1}. {item}")


shopping = []
choice = int(input("Choose 1 to print, choose 2 to add item, choose 3 to remove item."))
if choice == 1:
    printed_list(shopping)
elif choice == 2:
    add_item(shopping, "item")
elif choice == 3:
    remove_item(shopping, "item")

while choice == 2:
    user_input = input("Would you like to add another item to the list? yes/no ").lower()
    if user_input == "yes":
        new_item = input("Which other item would you like to add?")
        add_item(shopping, new_item)
    elif user_input == "no":   
        user_choice = input("Which other choice can I help you with? 1/3")
        if user_choice == "1":
            printed_list(shopping, "item")
        elif user_choice == "3":
            new_item = input("Which item would you like to remove? ")
            remove_item(shopping, new_item)
        else:
            print("Thank you for using my app to make your list!")
            break
else:
    print("Please enter a valid response: yes or no.")





  


        



    

    




