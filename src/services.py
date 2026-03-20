incomes = []
expenses = []


def add_transaction(transaction_type, amount, description):
    transaction = {"amount": amount, "description": description}

    if transaction_type == "income":
        incomes.append(transaction)
    else:
        expenses.append(transaction)


def list_transactions():
    return incomes, expenses


def calculate_balance():
    total_income = sum(i["amount"] for i in incomes)
    total_expenses = sum(e["amount"] for e in expenses)
    return total_income - total_expenses


def delete_transaction(transaction_type, index):
    data_list = incomes if transaction_type == "income" else expenses

    if 0 <= index < len(data_list):
        data_list.pop(index)
        return True
    return False


def edit_transaction(transaction_type, index, amount, description):
    data_list = incomes if transaction_type == "income" else expenses

    if 0 <= index < len(data_list):
        data_list[index]["amount"] = amount
        data_list[index]["description"] = description
        return True
    return False
