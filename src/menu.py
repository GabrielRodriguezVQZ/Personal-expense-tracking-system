#show main menu options to user
def show_menu():
    print("\n--- MENU ---")
    print("1. Register income")
    print("2. Register expense")
    print("3. List transactions")
    print("4. Show balance")
    print("5. Edit transaction")
    print("6. Delete transaction")
    print("0. Exit")

#get user input for menu option
def get_option():
    try:
        option = int(input("Select an option: "))
        return option
    except ValueError:
        print("Invalid input")
        return -1