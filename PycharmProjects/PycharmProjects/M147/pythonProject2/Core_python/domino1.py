'''
Project Description: Domino's Clone Application
In this project, we will build a Domino's Clone Application using Object-Oriented Programming (OOP) in Python with a database connection to manage customer information and orders. Each customer will be treated as an object, and the application will include functionalities for sign-up, login, ordering food, viewing the cart, and displaying the bill.
________________________________________
Key Functionalities:
1.	Signup:
•	New users can register by providing their details.
•	User information will be stored in a database (e.g., SQLite or MySQL).
2.	Login:
•	Users can log in using their credentials.
•	If the credentials do not exist in the database, the user will be prompted to sign up.
3.	Display Menu:
•	The items should get displayed
4.	Order Food:
•	Users can browse a menu and place an order.
•	The selected items will be added to their cart.
5.	View Cart:
•	Users can view the items added to their cart.
6.	Display Bill:
•	The total bill will be generated based on the items in the cart.
•	The bill will display item details, quantities, and total cost.
________________________________________

'''
import sqlite3
conn = sqlite3.connect('Dominos.db')
cou = conn.cursor()
# cou.execute('CREATE TABLE USER (UN VARCHAR(20) ,PWS VARCHAR(20),EMAIL VARCHAR(30))')
# cou.execute('INSERT INTO USER VALUES("ANNA","123456","ABC@1999.com")')
# conn.commit()

class Dominos:
    menu = [
        {'id': 1, 'name': "Margherita Pizza", "price": [99, 199, 399]},
        {'id': 2, 'name': "Pepperoni Pizza", "price": [169, 309, 499]},
        {'id': 3, 'name': "Vegetarian Pizza", "price": [119, 299, 399]},
        {'id': 4, 'name': "Hawaiian Pizza", "price": [349, 425, 498]},
        {'id': 5, 'name': "BBQ Chicken Pizza", "price": [390, 449, 529]},
        {'id': 6, 'name': "Meat Lovers Pizza", "price": [199, 299, 499]},
        {'id': 7, 'name': "Supreme Pizza", "price": [229, 499, 699]}]
    coke = [
        {'id': 8, "name": "Coca Cola", "price": 90},
        {'id': 9, "name": "Sprite", "price": 50},
        {'id': 10, "name": "Fanta", "price": 30},
        {'id': 11, "name": "Root Beer", "price": 90.9}]
    def __init__(self):
        self.cart = []
        self.signed = False
        self.log = False

    def Doiminos_menu(self):
        while True:
            print('----------------------WELCOME TO--------------------')
            print('enter 1 :signup')
            print('enter 2 :login')
            print('enter 3 :logout')
            if self.log == True:
                print('Enter 4: Order')
                print('Enter 5: Open Cart')
                print('Enter 6: Display Bill')
                print('Enter 7: Remove Items')
            choice = int(input('Enter your choice: '))
            if choice == 1:
                self.signup()
            elif choice == 2:
                self.login()
            elif choice == 3:
                self.logout()
                break
            elif choice == 4:
                self.order()
            elif choice == 5:
                self.open_cart()
            elif choice == 6:
                self.disp_bill()
            elif choice == 7:
                self.edit_cart()
            a = input('Do you want to continue (y/n): ')
            if a.lower() == 'y':
                continue
            else:
                break
    def signup(self):
        if self.signed == False:
            e = list(cou.execute('select email from user'))
            l = list(cou.execute('select un from user'))
            while True:
                email = input('enter the mail:')
                if (email,) not in e:
                    un = input('enter the username:')
                    if (un,) not in l:
                        while True:
                            pwd1 = input('enter the password:')
                            pwd2 = input('confirm the password:')
                            if pwd1==pwd2:
                                cou.execute(f'''INSERT INTO USER VALUES("{un}","{pwd1}","{email}")''')
                                conn.commit()
                                print('Signup Successful\n')
                                self.signed = True
                                break
                            else:
                                print("Password doesn't match")

                    else:
                        print('Username available')
                        continue
                else:
                    print('Email already Exist\n')
                    continue
                break
        else:
            print('Already signed up...\n')


    def login(self):
        e = list(cou.execute('select email from user'))
        u = list(cou.execute('select un from user'))
        print('Enter 1: Login with Email..')
        print('Enter 2: Login with User Name..')
        choice = int(input('enter your email: '))
        if choice==1:
            email = input('enter your email:')
            pwd = input('enter your password:')
            if (email,) in e:
                if pwd in list(cou.execute(f'select pwd from yser whrer email = "{email}"')):
                    print('Login successful')
                    self.log = True
                else:
                    print('Incorrect Password')
                    self.login()

            else:
                print('your email doesnot exist')
                n = input('Do you want to sign up y/n: ')
                if n.lower() == 'y':
                    self.signup()
                else:
                    print('Have a nice day!!')
        elif choice == 2:
            un = input('Enter your User name: ')
            pwd = input('Enter your password: ')
            if (un,) in u:
                if (pwd,) in list(cou.execute(f'SELECT PWD FROM USER WHERE UN="{un}"')):
                    print('Login successful\n')
                    self.log = True
                else:
                    print('Incorrect Password')
                    self.login()
            else:
                print('Your username does not exist\n')
                n = input('Do you want to sign up y/n: ')
                if n.lower() == 'y':
                    self.signup()
                else:
                    print('Have a nice day!!')
        else:
            print('Invalid choice\n')
            self.login()
    def logout(self):
        self.log = False
        print('Logout successful')

    def order(self):
        if self.log == True:
            print('Enter 1: order Pizza')
            print('Enter 2: order Cokes')
            ch = int(input('Enter your choice: '))
            if ch==1:
                self.order_pizza()
            elif ch==2:
                self.order_coke()
            else:
                print('invalid choice')
                self.order()
        else:
            print('Login Required....')
            self.login()
    def order_coke(self):
        for i in Dominos.coke:
           l = len(str(i['id']))+len(i['name'])
           print(i['id'],'--',i['name'],' '*(20-l),i['price'],'Rs.')

        choice = int(input('enter the choice:'))
        if choice in [8,9,10,11]:
            qty = int(input('enter the quantity: '))
            for j in Dominos.coke:
                if j['id'] == choice:
                    for k in self.cart:
                        if k['id'] == j['id']:
                            k['quantity'] += qty
                            k['price']+=(j['price'])*qty
                            break
                    else:
                        self.cart.append(j)
            print('Item Added to your cart...\n')
            ch = input('Do you want to add more...? (Type: y/n): ')
            if ch.lower() == 'y':
                self.order()
        else:
            print('Invalid choice ... please Enter valid choice\n')
            self.order_coke()

    def order_pizza(self):
        print('item','regular','medium','Large')
        print('--------------------------------')
        for i in Dominos.menu:
            l = len(str(i['id'])) +len(i['name'])
            print(i[id],'--',i['name'],' '*(25-l),'--',i['price'][0],'Rs.')
            choice = int(input('Enter your choice: '))
            if choice in [1, 2, 3, 4, 5, 6, 7]:
                print('Enter 1: Regular')
                print('Enter 2: Medium')
                print('Enter 3: Large')
                ch = int(input('Enter your choice: '))
                l = ['Reg', 'Med', 'Lar']
                qty = int(input('Enter Pizza Quantity: '))
                for i in Dominos.menu:
                    if i['id']==choice:
                        for j in self.cart:
                            if i['id'] == j['id']:
                                j['Quantity'] += qty
                                j['price'] += (i['price'][ch - 1]) * qty
                                break
                        else:
                            self.cart.append((j))
                            if ch == 1:
                                self.cart[-1]['price'] = (i['price'][0]) * qty
                                self.cart[-1]['cat'] = 'Reg'
                            elif ch == 2:
                                self.cart[-1]['price'] = (i['price'][1]) * qty
                                self.cart[-1]['cat'] = 'Med'
                            elif ch == 3:
                                self.cart[-1]['price'] = (i['price'][2]) * qty
                                self.cart[-1]['cat'] = 'Lar'
                            else:
                                print('Invalid choice')
                                self.order_pizza()
                print('Item Added to your cart...\n')
                ch = input('Do you want to add more...? (Type: y/n): ')
                if ch.lower() == 'y':
                    self.order()
            else:
                print('Invalid choice ... please Enter valid choice\n')
                self.order_pizza()
    def disp_bill(self):
        amt = 0
        qty = 0
        if self.log == True:
            print('--------------------DOMINOS PIZZA----------------------')
            print('------------------------BILL---------------------------')
            for i in self.cart:
                l = len(str(i['id'])) + len(i['name'])
                print(i['name'], ' ' * (25 - l), f'({i['cat']})', i['Quantity'], '--------', i['price'], ' Rs.')
                amt += i['price']
                qty += i['Quantity']
            print('Total :  ',' '*17,qty,'--------',round(amt,3),' Rs.')
        else:
            print('Login Required....\n')
            self.login()






