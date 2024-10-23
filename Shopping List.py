def add_item(my_list):
    item = input("Which item would you like to add: ")
    my_list.append(item)

def remove_item(my_list):
    item = input("Which item would you like to remove: ")
    if item in my_list:
        my_list.remove(item)
        print(f"{item} has been removed from the list.")
    else:
        print("Item is not on the list.")

def printed_list(my_list):
    if not my_list:
        print("The list is empty.")
    else:
        print("List contents:")
        for i, item in enumerate(my_list):
            print(f"{i+1}. {item}")

shopping = []

while True:
    print("\nMenu Options:")
    print("1. Print the shopping list")
    print("2. Add an item to the shopping list")
    print("3. Remove an item from the shopping list")
    print("4. Exit")

    choice = input("Choose an option (1/2/3/4): ")

    if choice == "1":
        printed_list(shopping)
    elif choice == "2":
        add_item(shopping)
    elif choice == "3":
        remove_item(shopping)
    elif choice == "4":
        print("Thank you for using the shopping list app. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
