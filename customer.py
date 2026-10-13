import store_data
from store_data import prevent_error
products = store_data.products
cart = store_data.cart
customer_info = store_data.customer_info
def customer_menu():
    print("-"*50)
    customer_menu=["===== WELCOME TO SMART STORE =====\n","1) View products\n","2) Search products\n","3) Add products to cart\n","4) View cart\n","5) Update cart\n","6) Place order\n","7) Exit\n","="*33]
    for i in range(len(customer_menu)):
        print(customer_menu[i])

    print("-" * 50)
def pro_menu():
    print("""===================================
*******WELCOME TO SMART STORE*******
====================================
(  ID |     Name     | Amount | Stock )
-------------------------------------""")
    for item in products.values():
        print("   ", item["ID"], "|", item["name"], "|", item["amount"], "    | ", item["stock"], "|", "\n")
        print("-------------------------------------")

def search_product():
    search_pro_user = input("enter the product name :")
    user_pro = (search_pro_user.upper())
    found = False
    for outer_key, inner_dict in products.items():
        if user_pro == inner_dict["name"]:
            print("=====================================")
            print("Your search product ID is :", inner_dict["ID"])
            print("Your search product name  :", inner_dict['name'], "\n")
            print(" Product amount    :", inner_dict['amount'], "\n")
            print(" Stocks available  : ", inner_dict['stock'], "\n")
            print("======================================\n")
            found = True
            menu_txt=("""
                                                        Do you want add this product to cart ?

                                                              1) yes 
                                                              2) No
                                                                 Enter your choice :""")
            user_pur_choice = prevent_error(menu_txt)

            if user_pur_choice == 1:
                quantity_txt = "Enter the quantity of the product :"
                quantity = prevent_error(quantity_txt)
                result = add_to_cart(inner_dict["ID"], quantity)
                if result is False:
                    print("Your product failed to add to cart!")
                else:
                    print("=" * 30)
                    print("\nYour product is added to cart !!")
                break
            elif user_pur_choice == 2:
                print("Thank you for visiting our store !!\n")
                break
            else:
                print("Invalid choice !!")
                break

    if found == False:
            print("your item is not found !!")
            print("-" * 40, "\n")
def add_to_cart(product_id,quantity):
    product=products[product_id]
    if quantity<=0:
        print("The quantity is must be greater than 0, Please enter a valid quantity!")
        return False
    elif quantity > product["stock"]:
         print(f"Sorry,we only have {product['stock']} stock in this product. Please enter small quantity number (or) wait for restock!")
         return False
    else:
            total_amount = quantity * product["amount"]
            if product_id in cart:
                cart[product_id]["quantity"] += quantity
                cart[product_id]["total_amount"] += total_amount
                products[product_id]["stock"] -= quantity

            else:
                cart[product_id] = {
                    "name": product["name"],
                    "amount": product["amount"],
                    "quantity": quantity,
                    "total_amount": total_amount,
                }
                products[product_id]["stock"] -= quantity



def view_pro():
    pro_menu()

def add_pro_cart():
    pro_menu()
    user_products=0

    print("*** Please check the above product list ***\n")
    user_products_txt = ("Enter the product ID:")
    user_products=prevent_error(user_products_txt)
    if user_products in products:
        print("Your product is available !\n")
        print("Product name   : ", products[user_products]["name"], "\n")
        print("Product amount : ", products[user_products]["amount"], "rs\n")
        print("Product stock  : ", products[user_products]["stock"], "stocks available \n")
        print("________________________________\n")
        product_to_cart_txt = ("""Do you want to add the product to cart ?

                         1) Yes
                         2) No
                            Enter your choice :""")
        product_to_cart = prevent_error(product_to_cart_txt)
        print("________________________________\n")

        if product_to_cart == 1:
            quantity_txt = ("Enter the quantity of the product :")
            quantity = prevent_error(quantity_txt)
            conform_pro_to_cart=add_to_cart(user_products,quantity)
            if conform_pro_to_cart==False:
                print("===================================")
                print("Your product is failed to add!!")
                print("===================================")
            else:
                print("====", quantity, products[user_products]["name"], "is added to cart !", "====")
                print("Your amount for this product :", quantity * products[user_products]["amount"], "rs\n")
                print("======= Your item is added to cart !========\n")
                print("=" * 30, "\n")
                print("Do you want to continue shopping ?")
                another_pro_txt = (""" ==========================
                                                      1) yes 
                                                      2) no 
                                                         Enter your choice :
                                                      """)
                another_pro = prevent_error(another_pro_txt)
                if another_pro == 1:
                    pro_menu()
                    add_pro_cart()
                else:
                    print("=" * 15)
                    print("YOUR PRODUCTS WAS ADDED TO CART !!\n")

                    print("THANK YOU FOR VISITING !!!\n")
                    print("=" * 15)
        elif product_to_cart == 2:
            print("***** Thank you for visiting *****")
        else:
            print("Invalid choice !")
            print("Please try again !!")
            pro_menu()
            add_pro_cart()
    else:
        print("Invalid product ID !")



def view_cart():
    if len(cart) == 0:
        print("The cart is empty !!,Add products to view cart")
    else:
        grand_total = 0
        print("============ Your cart ============\n")

        for product_id,item in cart.items():
         print("Product name    :", item["name"], "\n")
         print("Product quantity:", item["quantity"], "\n")
         print("Product amount    :", item["amount"], "\n")
         print("==================================\n=")
         grand_total+=item["total_amount"]
        print("=== Your Grand Total amount to pay : ", grand_total)
        print("========================================\n")
def update_cart():
    update_cart_ope_txt = ("""-------------------------------
                                   1) Add product
                                   2) Delete product
                                   3) Change quantity

                                      Enter your choice: 
                                   """)
    update_cart_ope=prevent_error(update_cart_ope_txt)
    if update_cart_ope == 1:
        pro_menu()
        user_products_txt = ("Enter the product ID:")
        user_products=prevent_error(user_products_txt)
        if user_products in products:
            print("Your product is available !\n")
            print("Product name   : ", products[user_products]["name"], "\n")
            print("Product amount : ", products[user_products]["amount"], "rs\n")
            print("Product stock  : ", products[user_products]["stock"], "stocks available \n")
            print("________________________________\n")
            product_to_cart_txt= ("""Do you want to add the product to cart ?

                                 1) Yes
                                 2) No
                                    Enter your choice :""")
            product_to_cart=prevent_error(product_to_cart_txt)
            print("________________________________\n")

            if product_to_cart == 1:

                quantity_txt = "Enter the quantity of the product :"
                quantity = prevent_error(quantity_txt)
                result = add_to_cart(user_products, quantity)
                if result is not False:
                    print("Your cart is updated !!")
            elif product_to_cart == 2:
                print("Your product in cart is not changed !!")
    elif update_cart_ope == 2:
        if len(cart) <=0:
            print("The cart is already empty !!")
        else:
            del_pro_txt = ("Enter the product ID to remove item :")
            del_pro=prevent_error(del_pro_txt)
            if del_pro in cart:
                del_item = cart.pop(del_pro)
                print(del_item)
                print("The", del_item["name"], "is removed from cart !!")
                products[del_pro]["stock"] +=del_item["quantity"]
            else:
                print("Invalid product ID (or) product is not available in cart !!")
    elif update_cart_ope == 3:
        update_quantity_id_txt= ("Enter the product id to change quantity :")
        update_quantity_id=prevent_error(update_quantity_id_txt)
        if update_quantity_id in cart:
            print(cart[update_quantity_id]["name"], "is available in your cart !!\n")
            print(cart[update_quantity_id]["quantity"], "quantity is available in your cart !!\n ")
            user_input_update_quantity_txt= ("""===============================
                                                        1) Add quantity
                                                        2) Reduce quantity
                                                           Enter your choice: """)
            user_input_update_quantity=prevent_error(user_input_update_quantity_txt)
            if user_input_update_quantity == 1:
                while True:
                    add_quantity_txt = ("Enter the number of quantity to add :")
                    add_quantity = prevent_error(add_quantity_txt)
                    if add_quantity <= 0:
                        print("Please enter a positive number!")
                    else:
                        if add_quantity > products[update_quantity_id]["stock"]:
                            print(
                                f"The product {products[update_quantity_id]["name"]} has {products[update_quantity_id]["stock"]} stock !!")
                            print("Please check the product list!!\n")
                            print("failed to update quantity !!\n")
                        else:
                            cart[update_quantity_id]["quantity"] += add_quantity
                            products[update_quantity_id]["stock"] -= add_quantity
                            cart[update_quantity_id]["total_amount"] += add_quantity * cart[update_quantity_id][
                                "amount"]
                            print("Your cart is updated !!")
                            break
            elif user_input_update_quantity == 2:
                reduce_quantity_txt= ("Enter the number of quantity to reduce :")
                reduce_quantity=prevent_error(reduce_quantity_txt)
                if reduce_quantity<=0:
                    print("Please enter quantity greater than 0, avoid negative numbers!!")
                elif reduce_quantity > cart[update_quantity_id]["quantity"]:
                    print("Your quantity is already lesser then your input quantity,Please check your cart\n")
                    print("=============================================================================")
                elif reduce_quantity == cart[update_quantity_id]["quantity"]:
                    print(f"The product {cart[update_quantity_id]["name"]} has quantity :{cart[update_quantity_id]["quantity"]}")
                    print("So, the product will be removed from your cart !!")
                    del cart[update_quantity_id]
                    products[update_quantity_id]["stock"]+=reduce_quantity
                else:
                    cart[update_quantity_id]["quantity"] -= reduce_quantity
                    cart[update_quantity_id]["total_amount"] -= reduce_quantity * cart[update_quantity_id]["amount"]
                    products[update_quantity_id]["stock"] += reduce_quantity
                    print("Your cart is updated !!")
    else:
        print("Invalid choice !!")


def place_order():
    print("Do you want to conform your purchase ? ")
    conform_purchase= ("""==========================
                                     1) yes 
                                     2) no 
                                        Enter your choice : """)
    con_purchase=prevent_error(conform_purchase)
    if con_purchase == 1:
        if len(cart) == 0:
            print("The cart is empty !!,Add products to view")
            print("Please add items to cart for purchase !!")
            return False
        elif len(cart)>0:
            print("===========================================")
            customer_info["name"] = input("Enter your name:")

            while True:
                customer_info["contact number"] = input("Enter your phone number:")
                if customer_info["contact number"].isdigit():
                    if len(customer_info["contact number"]) == 10:
                        print("Please verify your contact number!,the payment will be shared!")
                        print(f"{customer_info['name']}'s contact number : {customer_info['contact number']}")
                        break
                    else:
                        print("Please enter a valid 10 digit contact number!,the payment will be shared!")
                else:
                    print("Please enter a please enter digits only!!")

            customer_info["email ID"] = input("Enter your Email:")
            print("============================================")
            print("""The payment is shared to your mobile number !!
                                                     Accept payment and kindly pay your bill 

                                                     =======================================
                                                     ======== THANK YOU FOR PURCHASE =======
                                                     ===Come again !, Have a great day !!===\n""")
            cart.clear()
            return True


    else:
        print("Your purchase was cancelled !!")
        return False
def customer_side():
    running = True
    while running:
        customer_menu()
        customer_choice_txt= ("Enter your choice:")
        customer_choice=(prevent_error(customer_choice_txt))
        if customer_choice == 1:
            view_pro()
        elif customer_choice == 2:
            search_product()
        elif customer_choice == 3:
            add_pro_cart()
        elif customer_choice == 4:
            view_cart()
        elif customer_choice == 5:
            update_cart()
        elif customer_choice == 6:
            order_success = place_order()

            if order_success is True:
                after_pay_shopping_txt = (
                    "Do you want to continue shopping? 1) Yes  2) No: "
                )
                after_pay_shopping = prevent_error(after_pay_shopping_txt)
                if after_pay_shopping == 1:
                    running = True
                else:
                    print("""=====================================
                                              =======THANK YOU FOR VISITING!1 =======
                                              ========= HAVE A GREAT DAY ==========
                                              =====================================""")
                    running = False

                if after_pay_shopping == 1:
                    running = True
                elif after_pay_shopping == 2:
                    print("THANK YOU FOR VISITING! HAVE A GREAT DAY!")
                    running = False
                else:
                    print("Invalid choice!")
        elif customer_choice == 7:
            print("====Thank you for visiting !!====")
            running = False



