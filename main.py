from menu import show_menu, register, list_all, show_balance, edit, delete

while True:
    show_menu()
    option = input("Select an option: ")

    try:
        option = int(option)
    except:
        print("You must enter a number")
        continue

    match option:
        case 1:
            register("income")
        case 2:
            register("expense")
        case 3:
            list_all()
        case 4:
            showbalance()
        case 5:
            edit()
        case 6:
            delete()
        case 0:
            print("Goodbye")
            break
        case _ :
            print("Invalid option")