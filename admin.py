import store_data
from store_data import prevent_error
products = store_data.products   # shared data from store_data.py
def admin_menu():
    print("-" * 50)
    admin_menu=["===== WELCOME TO ADMIN CONSOLE =====\n","1) View current products\n","2) Add products\n","3) Remove product\n","4) Update amount of products\n","5) Update stock of product\n ","6) Exit\n","="*33]
    for i in range(len(admin_menu)):
        print(admin_menu[i])
    print("-" * 50)
def pro_menu():
    print("""===================================
*******WELCOME TO SMART STORE*******
====================================
(  ID |     Name     | Amount | Stock )
-------------------------------------""")
    for item in products.values():
        print("   ", item["ID"], "|", f"{item["name"]:^11} ", "|  ", item["amount"], "  | ", item["stock"], "|", "\n")
        print("-------------------------------------\n")
def add_product():
    while True:
        pro_name1= input("Enter product name to add : ").strip()

        if not pro_name1:
            print("Product name cannot be empty! Please try again.")
        else:
            break
    if pro_name1.isdigit():
        print("You entered an invalid product name")
        return
    else:

        pro_name = pro_name1.upper()
        exist_pro = []
        for outer_key,inner_dict in products.items():
            exist_pro.append(inner_dict["name"].strip().upper())

        if pro_name in exist_pro:
            print("The product name already exists\n")
            add_pro_update_txt=("""
            =====================================
            The product is already in the list!
            Do you want to update the existing product?
                    1) update amount of product
                    2) update stock of product
                    3) Exit to main menu
                       Enter your choice:""")
            add_pro_update=prevent_error(add_pro_update_txt)
            if add_pro_update==1:
                change_amount()
            elif add_pro_update==2:
                update_stock()
            elif add_pro_update==3:
                pass
            else:
                print("Invalid choice! Please select 1, 2, or 3.")

        else:
            proname = pro_name.strip().upper()
            print("="*25)
            pro_amount_txt = "Enter product amount:"
            while True:
                pro_amount = prevent_error(pro_amount_txt)
                if pro_amount <= 0:
                    print("Price must be greater than 0!")
                else:
                    break
            pro_stock_txt = "\nEnter product stock available:"
            while True:
                pro_stock = prevent_error(pro_stock_txt)
                if pro_stock < 0:
                    print("Stock cannot be negative!")
                else:
                    break

            print("=" * 25)
            existing_ID=list(products.keys())
            run=True
            while run:
             new_key_txt = (f"""
                        =================================
                        Enter a new ID for the new product 
                        * the existing ID :{existing_ID} 
                        * Don't use existing ID number
                        * Use Only numbers 
                        Please enter a new ID:""")
             new_key=prevent_error(new_key_txt)
             if new_key<=0:
                 print("The new ID number must be greater than 0,Please check above condition!!")
             elif new_key in products.keys():
                 print("That ID is already exist,try again!")
             else:
                 products[new_key] = {"ID": new_key, "name": proname, "amount": pro_amount, "stock": pro_stock}
                 run=False
def change_amount():
    pro_menu()
    pro_ID_txt= ("Enter product ID to update amount:")
    pro_ID=prevent_error(pro_ID_txt)
    if pro_ID in products.keys():
        new_amount_txt = ("Enter new amount:")
        while True:
            new_amount=prevent_error(new_amount_txt)
            if new_amount<=0:
                print("Price must be greater than 0!")
            else:
                products[pro_ID]["amount"] = new_amount
                print("the product amount has been updated !!\n")
                print(f"The amount of {products[pro_ID]["name"]} is updated to {products[pro_ID]['amount']} !!")
                break
    else:
        print("Invalid product ID! Please check the product list and try again.")

def update_stock():
    pro_menu()
    pro_ID_stock_txt=("Enter product ID to update stock:")
    pro_ID_stock=prevent_error(pro_ID_stock_txt)
    if pro_ID_stock in products.keys():
        new_stocks_txt = ("Enter new stock to update :")
        while True:
            new_stock=prevent_error(new_stocks_txt)
            if new_stock<0:
                print("The stock must be greater than 0,Please try again!!")
            else:
                products[pro_ID_stock]["stock"] = new_stock
                print(f"the {products[pro_ID_stock]['name']} stock has been updated to {products[pro_ID_stock]["stock"]}!!\n")
                break
    else:
        print("invalid product ID")

def delete_product():
    pro_menu()
    while True:
        try:
            pro_id_del = int(input("Enter product ID to delete:"))
            if pro_id_del in products.keys():
                print("Yes the product is available !!")
                print("product name : ", products[pro_id_del]["name"])
                print("product stock: ", products[pro_id_del]["stock"], " stock is available!")
                while True:
                    try:
                        del_admin_choice = int(input("""
                                                               Do you want to remove this product?
                                                                       1) Yes
                                                                       2) No
                                                                          Enter your choice:"""))
                        if del_admin_choice == 1:
                            deleted_item = products.pop(pro_id_del)
                            print(f"The {deleted_item["name"]} has been removed from the list!!")
                            break
                        elif del_admin_choice == 2:
                            print(" Products are not removed from the list!!")
                            break
                        else:
                           print("Invalid choice! Please enter 1 or 2.")

                    except ValueError:
                        print("Please enter the choice correctly !!!!")
                break
            else:
                print("The product ID is invalid!!")

        except ValueError:
            print("Please enter a ID number!!")


def admin():
    running=True
    while running:
        admin_menu()
        admin_choice_txt=("enter admin menu choice:")
        admin_choice=prevent_error(admin_choice_txt)
        if admin_choice==1:
            pro_menu()
        elif admin_choice==2:
            add_product()
        elif admin_choice==3:
            delete_product()
        elif admin_choice==4:
            change_amount()
        elif admin_choice==5:
            update_stock()
        elif admin_choice==6:
            running=False
        else:
            print("Invalid choice! Please select a number from 1 to 6.")

