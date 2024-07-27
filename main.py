import uuid
import pymongo

class Product:
    def __init__(self, id, name, price, desc=""):
        self.Id = id
        self.Name = name
        self.price = price
        self.desc = desc

def list_cart(cart_list):
    for product_Id in cart_list:
        match = next(obj for obj in product_list if obj.Id == product_Id)
        print(match.Name)

def insert_product():
    new_name = input("\nName: ")
    new_price = int(input("Price: "))
    new_description = input("Description: ")
    product_list.append(Product(str(uuid.uuid4()), new_name, new_price, new_description))
    my_product = {"name": new_name, "price": new_price, "description": new_description}
    x = collection.insert_one(my_product)

def menu(collection):
    menu_choice = 0
    login_password = ""
    login_password = input("Password: ")
    if login_password == "321":
        while menu_choice != 1:
            menu_choice = input("\nSelect a option:\n[1] exit\n[2] add a product\n[3] take out a product\n[4] update a product\n")
            if int(menu_choice) == 1:
                print("\nThank you for using WebMarketPlace\n")
                break
            if int(menu_choice) == 2:
                def insert_product():
                    new_name = input("\nName: ")
                    new_price = int(input("Price: "))
                    new_description = input("Description: ")
                    product_list.append(Product(str(uuid.uuid4()), new_name, new_price, new_description))
                    my_product = {"name": new_name, "price": new_price, "description": new_description}
                    x = collection.insert_one(my_product)

            if int(menu_choice) == 3:
                product_list.pop(int(input("Select the position of the product you want to remove: ")) - 1)
            if int(menu_choice) == 4:
                product_update = int(input("Select the position of the product you want to update: ")) - 1
                print(product_list[product_update].Name)
                product_list[product_update].Name = input("New name: ")
                product_list[product_update].price = int(input("New price: "))
                product_list[product_update].desc = input("New description: ")

    if login_password == "123":
        while menu_choice != 1:
            menu_choice = input("\nSelected a option:\n[1] exit\n[5] buy product\n[6] see cart\n")
            if int(menu_choice) == 1:
                print("\nThank you for using WebMarketPlace\n")
                break
            if int(menu_choice) == 5:
                product_buy = int(input("Select the position of the product you want to buy: ")) - 1
                product_quantity = int(input("Select the quantity of the product you want to buy: "))
                product_quantity = str(product_quantity)
                cart.append(product_list[product_buy].Id)
            if int(menu_choice) == 6:
                list_cart(cart)

if __name__ == '__main__':
    # region declaretions
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    database = myclient["WebMarketPlaceEnterprising"]
    collection = database["Product.py"]

    product_list = []
    cart = []
    product_list.append(Product("5a3461b3-a165-42e9-a675-aebd52abe14b", "Monitor Dell 27\"", 800, "27 polegadas, FHD, 75hz"))
    product_list.append(Product("f283b633-12aa-4ad4-a57e-78b3f9cc5724", "Mouse Logitech 703", 350, "Mouse Logitech 703 com 6 botões personalizáveis e dpi ajustável até em 15.000"))
    product_list.append(Product("987ae892-ed3c-416e-9a43-f996d7dc89e5", "Smartwatch Apple series 8", 6200, "Bluetooth, 40mm, preto"))
    product_list.append(Product("987ae892-ed3c-416e-9a43-f996d7dc89e7", "Iphone 13 Pro", 4000, "128gb"))
    product_list.append(Product("987ae892-ed3c-416e-9a43-f996d7dc89e8", "Iphone 13 Pro", 6500, "256gb"))
    # endregion
    menu(collection)

for product in product_list:
    print("\nId: {3}\nName: {0}\nPrice: {1}\nDescription: {2}".format(product.Name, product.price, product.desc, product.Id))
