inventory = []
def add_car():
    brand = input("Enter Brand Name: ")
    model = input("Enter Model Name: ")
    year = input("Enter Year: ")
    price = input("Enter Price: ")

    car = {
    "Brand: " : brand,
    "Model: " : model,
    "Year: " : year,
    "Price: " : price
    }
    inventory.append(car)
    print("successflly added")

def view_inventory():
    if len(inventory) == 0:
        print("No cars available")
    else:
        for cars in inventory:
            print("Brand: ", cars["Brand: "] )
            print("Model: ", cars["Model: "] )
            print("Year: ", cars["Year: "] )
            print("Price: ", cars["Price: "] )

def search_car():
    if len(inventory) == 0:
        print("No cars available")
    else:
        brand = input("Enter Brand Name: ")

        for car in inventory:
            if car["Brand: "].lower() == brand.lower():
                print("Brand: " , car["Brand: "] )
                print("Model: ", car["Model: "] )
                print("Year: ", car["Year: "] )
                print("Price: ", car["Price: "] )
            else:
                print("Not available")
def delete_car():
    if len(inventory) == 0:
        print("No cars available")
    else:
        brand = input("Enter Brand Name: ")
        for car in inventory:
            if car["Brand: "].lower() == brand.lower():
                inventory.remove(car)
                print("car deleted")
            else:
                print("Not available")
while True:
    print("Welcome to the Isaac's Inventory App")
    print("1. Add car")
    print("2. View Inventory")
    print("3. Search brand ")
    print("4. Delete car")
    print("5. Exit")
    try:
        choice = int(input("Select an option: "))
        if choice == 1:
            add_car()
        elif choice == 2:
            view_inventory()
        elif choice == 3:
            search_car()
        elif choice == 4:
            delete_car()
        elif choice == 5:
            print("Goodbye")
            break
        else:
            print("Invalid option")

    except ValueError:
        print("Select an option from 1 to 5")