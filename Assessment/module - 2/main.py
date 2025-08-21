from banker import Banker
from customer import Customer

def main():
    while True:
        print("\n==== BANK MENU ====")
        print("1. Banker Register")
        print("2. Banker Login")
        print("3. Customer Register")
        print("4. Customer Login")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Mobile No: ")
            password = input("Password: ")
            b = Banker(name=name, email=email, phone=phone, password=password)
            b.register()

        elif choice == "2":
            email = input("Email: ")
            password = input("Password: ")
            b = Banker()
            user = b.login(email, password)
            if user:
                print(f"  Welcome Banker {user[1]}")
                while True:
                    print("\n-- Banker Menu --")
                    print("1. View Customers")
                    print("2. Update Customer")
                    print("3. Delete Customer")
                    print("4. Logout")
                    ch = input("Enter choice: ")
                    if ch == "1":
                        b.view_customers()
                    elif ch == "2":
                        cid = input("Enter Customer ID: ")
                        new_name = input("New name: ")
                        new_email = input("New email: ")
                        new_phone = input("New Mobile No: ")
                        b.update_customer(cid, new_name, new_email, new_phone)
                    elif ch == "3":
                        cid = input("Enter Customer ID: ")
                        b.delete_customer(cid)
                    elif ch == "4":
                        break
            else:
                print("  Invalid banker login")

        elif choice == "3":
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Mobile No: ")
            password = input("Password: ")
            c = Customer(name=name, email=email, phone=phone, password=password)
            c.register()

        elif choice == "4":
            email = input("Email: ")
            password = input("Password: ")
            c = Customer()
            if c.login(email, password):
                print(f"  Welcome {c.name}")
                while True:
                    print("\n-- Customer Menu --")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. View Balance")
                    print("4. Logout")
                    ch = input("Enter choice: ")
                    if ch == "1":
                        amt = float(input("Enter amount: "))
                        c.deposit(amt)
                    elif ch == "2":
                        amt = float(input("Enter amount: "))
                        c.withdraw(amt)
                    elif ch == "3":
                        c.view_balance()
                    elif ch == "4":
                        break
            else:
                print("  Invalid customer login")

        elif choice == "5":
            print("-- Goodbye!")
            break
        else:
            print("  Invalid option")

if __name__ == "__main__":
    main()
