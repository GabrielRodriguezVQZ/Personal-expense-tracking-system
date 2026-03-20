from menu import show_menu, register, list_all, show_balance, edit, delete
from validations import validate_option


def main():
    while True:
        show_menu()

        option = validate_option(input("Select an option: "))

        if option is None:
            print("Invalid option")
            continue

        match option:
            case 1:
                register("income")
            case 2:
                register("expense")
            case 3:
                list_all()
            case 4:
                show_balance()
            case 5:
                edit()
            case 6:
                delete()
            case 0:
                print("Goodbye")
                break


if __name__ == "__main__":
    main()