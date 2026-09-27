from config import (
    add_mobile,
    display_mobiles,
    search_mobile,
    update_mobile,
    delete_mobile
)


def dashboard():

    while True:

        print("\n")
        print("=" * 45)
        print(" MOBILE SHOP MANAGEMENT")
        print("=" * 45)

        print("1. Add Mobile")
        print("2. Display All Mobiles")
        print("3. Search Mobile")
        print("4. Update Mobile")
        print("5. Delete Mobile")
        print("6. Exit")

        print("=" * 45)

        choice = input("Enter your choice: ")

        match choice:

            case "1":
                add_mobile()

            case "2":
                display_mobiles()

            case "3":
                search_mobile()

            case "4":
                update_mobile()

            case "5":
                delete_mobile()

            case "6":

                print("\nThank you for using Mobile Shop Management.")
                break

            case _:

                print("Invalid choice. Please try again.")

