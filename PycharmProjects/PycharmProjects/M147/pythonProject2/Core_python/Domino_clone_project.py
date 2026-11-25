import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('domino_clone.db')
cursor = conn.cursor()

# Create the tables for customers, menu items, and orders
def create_tables():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS menu_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        menu_item_id INTEGER,
        quantity INTEGER,
        total_price REAL,
        FOREIGN KEY (customer_id) REFERENCES customers (id),
        FOREIGN KEY (menu_item_id) REFERENCES menu_items (id)
    )''')

    conn.commit()

create_tables()


class Customer:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.id = None

    def sign_up(self):
        cursor.execute('''
        INSERT INTO customers (name, email, password) 
        VALUES (?, ?, ?)
        ''', (self.name, self.email, self.password))
        conn.commit()
        print(f"Customer {self.name} signed up successfully!")

    def login(self, email, password):
        cursor.execute('''
        SELECT * FROM customers WHERE email=? AND password=?
        ''', (email, password))
        user = cursor.fetchone()
        if user:
            self.id = user[0]  # Set customer ID on successful login
            print(f"Welcome back, {user[1]}!")
        else:
            print("Invalid credentials!")


class Menu:
    @staticmethod
    def display_menu():
        cursor.execute('SELECT * FROM menu_items')
        items = cursor.fetchall()
        print("Menu Items:")
        for item in items:
            print(f"{item[0]}. {item[1]} - ${item[2]:.2f}")

    @staticmethod
    def add_menu_item(name, price):
        cursor.execute('''
        INSERT INTO menu_items (name, price)
        VALUES (?, ?)
        ''', (name, price))
        conn.commit()
        print(f"Menu item {name} added successfully!")


class Order:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.items = []

    def add_to_cart(self, menu_item_id, quantity):
        cursor.execute('''
        SELECT price FROM menu_items WHERE id=?
        ''', (menu_item_id,))
        item = cursor.fetchone()
        if item:
            total_price = item[0] * quantity
            self.items.append((menu_item_id, quantity, total_price))
            print(f"Added {quantity} of item {menu_item_id} to the cart.")
        else:
            print("Invalid menu item.")

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            total = 0
            print("Your Cart:")
            for item in self.items:
                cursor.execute('''
                SELECT name FROM menu_items WHERE id=?
                ''', (item[0],))
                menu_item = cursor.fetchone()
                print(f"{menu_item[0]} - Quantity: {item[1]} - Total: ${item[2]:.2f}")
                total += item[2]
            print(f"Total Bill: ${total:.2f}")

    def place_order(self):
        if not self.items:
            print("Your cart is empty!")
            return

        total_bill = 0
        for item in self.items:
            cursor.execute('''
            INSERT INTO orders (customer_id, menu_item_id, quantity, total_price)
            VALUES (?, ?, ?, ?)
            ''', (self.customer_id, item[0], item[1], item[2]))
            total_bill += item[2]
        conn.commit()
        print(f"Order placed successfully! Your total bill is ${total_bill:.2f}")
        self.items.clear()


# Example menu items to be added to the database (you can adjust or remove this part)
def add_sample_menu_items():
    items = [
        ('Pizza Margherita', 10.99),
        ('Pepperoni Pizza', 12.99),
        ('Veggie Pizza', 11.49),
        ('Cheese Garlic Bread', 4.99),
        ('Coca Cola', 1.99)
    ]
    for item in items:
        Menu.add_menu_item(item[0], item[1])


add_sample_menu_items()


def main():
    while True:
        print("\nDomino Clone App")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            customer = Customer(name, email, password)
            customer.sign_up()

        elif choice == '2':
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            customer = Customer("", email, password)
            customer.login(email, password)

            if customer.id:  # Only proceed if login is successful
                while True:
                    print("\nMenu Options:")
                    print("1. Display Menu")
                    print("2. Order Food")
                    print("3. View Cart")
                    print("4. Place Order")
                    print("5. Log Out")
                    option = input("Choose an option: ")

                    if option == '1':
                        Menu.display_menu()
                    elif option == '2':
                        menu_item_id = int(input("Enter Menu Item ID: "))
                        quantity = int(input("Enter quantity: "))
                        order = Order(customer.id)
                        order.add_to_cart(menu_item_id, quantity)
                    elif option == '3':
                        order.view_cart()
                    elif option == '4':
                        order.place_order()
                    elif option == '5':
                        break
                    else:
                        print("Invalid option.")

        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == '__main__':
    main()
