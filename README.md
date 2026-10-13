# shopflow-python
# 🛒 Smart Store – Python Console Project

Smart Store is a console-based shopping application built using Python. I created this project to improve my understanding of Python basics by applying them in a practical project instead of only learning them through theory.

This project helped me understand how different Python concepts work together to build a simple shopping system, from browsing products to managing a cart and calculating the final bill.

## ✨ Features

### 🛍️ Customer Features
- View and search for available products.
- Add products to the shopping cart.
- Update product quantities in the cart.
- Remove products from the cart.
- View the cart and calculate the total bill.
- Place or cancel an order.
- Collect basic customer details during checkout.

### 🔧 Admin Features
- Add new products to the store.
- Manage product prices and stock quantities.
- Update the available stock.
- View and manage product information.

### 📦 Stock and Cart Management
- Stock decreases when products are added to the cart.
- Stock is restored when products are removed.
- The application checks product availability and validates user input.

## 🧠 Python Concepts I Practiced

One of my main goals in creating this project was to strengthen my Python fundamentals. I used the following concepts:

| Python Concept | How I Used It |
|---|---|
| **Variables** | Store product details, prices, quantities, and customer information. |
| **Lists** | Manage collections of products and cart items. |
| **Dictionaries** | Store product details and access information using keys. |
| **Functions** | Divide the program into smaller tasks, such as searching products and updating stock. |
| **Conditional Statements** | Make decisions based on user choices, product availability, and input validation. |
| **Loops** | Keep menus running and allow users to continue shopping or managing the store. |
| **Input Handling** | Accept choices and details from customers and administrators. |
| **Exception Handling** | Handle basic input errors and prevent some invalid inputs from interrupting the program. |
| **Modules and Imports** | Separate the code into different Python files to keep the project organized. |

## 📁 Project Structure

The project is divided into separate Python files so that each file handles a specific responsibility.

```text
Smart-Store/
│
├── main-1.py       # Main entry point of the application
├── customer.py     # Customer shopping and checkout functions
├── admin.py        # Product and stock management
├── store_data.py   # Shared product, cart, and customer data
└── README.md       # Project documentation
```

## 🚀 How to Run

**Requirements**
- Python 3 installed on your computer.
- A terminal or command prompt.

**Steps**

1. Clone or download this repository.
2. Open the project folder in your terminal.
3. Run the following command:

```bash
python main-1.py
```

If your system uses `python3` to run Python, use:

```bash
python3 main-1.py
```

The main menu will appear in the terminal, allowing you to choose the customer or admin section.

## 🎯 Why I Created This Project

I created Smart Store because I wanted to master the basics of Python through practical implementation.

While learning Python, I realized that understanding individual concepts is different from using them together in a working application. This project gave me an opportunity to practice functions, lists, dictionaries, loops, conditions, and input validation in one place.

I also learned the importance of organizing code into modules, managing shared data, and checking how one action affects another part of the program.

This is a learning project, and building it has helped me improve my problem-solving skills and confidence in Python.

## 🔮 Future Improvements

Some improvements I would like to explore as I continue learning Python are:

- Save product and order data permanently using a file or database.
- Apply Object-Oriented Programming (OOP).
- Add customer login and authentication.
- Maintain order history.
- Improve product search and filtering.
- Add a graphical user interface in a future version.

## 👨‍💻 About

**Smart Store** is a personal learning project developed to practice Python fundamentals through a practical application.

I am continuing to improve my Python skills and will use this project as a foundation for learning more advanced concepts.

*Built with Python 🐍*
