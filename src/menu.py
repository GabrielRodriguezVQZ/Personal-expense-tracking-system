#import functions from other modules
from services import (
    add_transaction,
    list_transactions,
    calculate_balance,
    delete_transaction,
    edit_transaction
)
from validations import validate_amount


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


#register a new transaction
def register(transaction_type):
    amount_input = input("Enter amount: ")
    amount = validate_amount(amount_input)  # validate number

    if amount is None:
        print("Invalid amount")
        return

    description = input("Description: ")
    if description.strip() == "":
        print("Empty description")
        return

    #save transaction
    add_transaction(transaction_type, amount, description)
    print("Transaction registered")


#show all transactions
def list_all():
    incomes, expenses = list_transactions()

    print("\n--- INCOME ---")
    if not incomes:
        print("No income")
    else:
        for i, t in enumerate(incomes, 1):
            print(f"{i}. {t['amount']} - {t['description']}")

    print("\n--- EXPENSES ---")
    if not expenses:
        print("No expenses")
    else:
        for i, t in enumerate(expenses, 1):
            print(f"{i}. {t['amount']} - {t['description']}")


#edit a transaction
def edit():
    transaction_type = input("Edit income or expense?: ").lower()

    incomes, expenses = list_transactions()
    data_list = incomes if transaction_type == "income" else expenses

    if not data_list:
        print("No data")
        return

    #show list
    for i, t in enumerate(data_list, 1):
        print(f"{i}. {t['amount']} - {t['description']}")

    try:
        index = int(input("Number to edit: ")) - 1
    except:
        print("Invalid input")
        return

    #new values
    amount = validate_amount(input("New amount: "))
    if amount is None:
        print("Invalid amount")
        return

    description = input("New description: ")
    if description.strip() == "":
        print("Empty description")
        return

    #update transaction
    if edit_transaction(transaction_type, index, amount, description):
        print("Edited successfully")
    else:
        print("Invalid index")


#delete a transaction
def delete():
    transaction_type = input("Delete income or expense?: ").lower()

    incomes, expenses = list_transactions()
    data_list = incomes if transaction_type == "income" else expenses

    if not data_list:
        print("No data")
        return

    #show list
    for i, t in enumerate(data_list, 1):
        print(f"{i}. {t['amount']} - {t['description']}")

    try:
        index = int(input("Number to delete: ")) - 1
    except:
        print("Invalid input")
        return

    #remove transaction
    if delete_transaction(transaction_type, index):
        print("Deleted successfully")
    else:
        print("Invalid index")


#show total balance
def show_balance():
    print("Total balance:", calculate_balance())