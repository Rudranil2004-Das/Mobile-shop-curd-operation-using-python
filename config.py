mobiles = []


'''
 ------------------------------------------------------------
 Adds a new mobile to the list
 ------------------------------------------------------------
'''
def add_mobile():

    print("\n========== ADD MOBILE ==========")

    mobile_id = int(input("Enter Mobile ID: "))

    for mobile in mobiles:

        if mobile[0] == mobile_id:

            print("Mobile ID already exists.")
            return

    brand = input("Enter Brand: ")
    model = input("Enter Model: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))

    mobile = [mobile_id, brand, model, price, quantity]

    mobiles.append(mobile)

    print("Mobile added successfully.")


'''
 ------------------------------------------------------------
 Displays all mobile records
 ------------------------------------------------------------
'''
def display_mobiles():

    print("\n========== MOBILE LIST ==========")

    if len(mobiles) == 0:

        print("No mobile records available.")
        return

    print("-" * 75)

    print(
        f"{'ID':<8}"
        f"{'Brand':<15}"
        f"{'Model':<20}"
        f"{'Price':<15}"
        f"{'Quantity':<10}"
    )

    print("-" * 75)

    for mobile in mobiles:

        print(
            f"{mobile[0]:<8}"
            f"{mobile[1]:<15}"
            f"{mobile[2]:<20}"
            f"{mobile[3]:<15.2f}"
            f"{mobile[4]:<10}"
        )

    print("-" * 75)


'''
 ------------------------------------------------------------
 Searches for a mobile by ID
 ------------------------------------------------------------
'''
def search_mobile():

    print("\n========== SEARCH MOBILE ==========")

    mobile_id = int(input("Enter Mobile ID to search: "))

    found = False

    for mobile in mobiles:

        if mobile[0] == mobile_id:

            print("\nMobile Found!")
            print("Mobile ID :", mobile[0])
            print("Brand :", mobile[1])
            print("Model :", mobile[2])
            print("Price :", mobile[3])
            print("Quantity :", mobile[4])

            found = True
            break

    if found == False:

        print("Mobile not found.")


'''
 ------------------------------------------------------------
 Updates an existing mobile
 ------------------------------------------------------------
'''
def update_mobile():

    print("\n========== UPDATE MOBILE ==========")

    mobile_id = int(input("Enter Mobile ID to update: "))

    for mobile in mobiles:

        if mobile[0] == mobile_id:

            print("\nMobile Found.")

            print("Current Brand :", mobile[1])
            print("Current Model :", mobile[2])
            print("Current Price :", mobile[3])
            print("Current Quantity :", mobile[4])

            print("\nEnter New Details")

            new_brand = input("Enter New Brand: ")
            new_model = input("Enter New Model: ")
            new_price = float(input("Enter New Price: "))
            new_quantity = int(input("Enter New Quantity: "))

            mobile[1] = new_brand
            mobile[2] = new_model
            mobile[3] = new_price
            mobile[4] = new_quantity

            print("Mobile updated successfully.")
            return

    print("Mobile not found.")


'''
 ------------------------------------------------------------
 Deletes a mobile from the list
 ------------------------------------------------------------
'''
def delete_mobile():

    print("\n========== DELETE MOBILE ==========")

    mobile_id = int(input("Enter Mobile ID to delete: "))

    for mobile in mobiles:

        if mobile[0] == mobile_id:

            print("\nMobile Found.")
            print("Brand :", mobile[1])
            print("Model :", mobile[2])

            choice = input(
                "Do you want to delete this mobile? (Y/N): "
            )

            if choice.upper() == "Y":

                mobiles.remove(mobile)

                print("Mobile deleted successfully.")

            else:

                print("Delete operation cancelled.")

            return

    print("Mobile not found.")


