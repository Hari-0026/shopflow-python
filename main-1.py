# main.py - the starting point of the Smart Store program

import customer  
import admin     

def main_menu():
    print("\n====== WELCOME TO SHOPFLOW STORE SYSTEM ======")
    print("=========================================")
    print("1) I am a customer")
    print("2) I am an admin")
    print("3) Exit")
    print("=========================================")


def main():
    running = True
    while running:
        main_menu()

        # The choice is read INSIDE the loop, so the menu asks again every time.
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number (1, 2 or 3)!!")
            continue

        if choice == 1:
            customer.customer_side()
        elif choice == 2:
            admin.admin()
        elif choice == 3:
            print("Thank you for visiting !!")
            running = False
        else:
            print("Invalid choice")


# Runs only when you start this file directly (python main.py),
# not when another file imports it.
if __name__ == "__main__":
    main()
