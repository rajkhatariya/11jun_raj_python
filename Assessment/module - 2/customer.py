from db_connection import get_connection

class Customer:
    def __init__(self, customer_id=None, name=None, email=None, phone=None, password=None):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.__balance = 0   

    def register(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO customer (name, email, phone, password, balance) VALUES (%s,%s,%s,%s,0.00)",
                    (self.name, self.email, self.phone, self.password))
        conn.commit()
        print(" Customer registered successfully")
        conn.close()

    def login(self, email, password):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT customer_id, name, balance FROM customer WHERE email=%s AND password=%s",
                    (email, password))
        row = cur.fetchone()
        conn.close()
        if row:
            self.customer_id, self.name, self.__balance = row
            return True
        return False

    def deposit(self, amount):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("UPDATE customer SET balance = balance + %s WHERE customer_id=%s",
                    (amount, self.customer_id))
        conn.commit()
        conn.close()
        print(f"  Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print(" Insufficient balance")
            return
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("UPDATE customer SET balance = balance - %s WHERE customer_id=%s",
                    (amount, self.customer_id))
        conn.commit()
        conn.close()
        print(f" Withdrawn ₹{amount}")

    def view_balance(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT balance FROM customer WHERE customer_id=%s", (self.customer_id,))
        row = cur.fetchone()
        conn.close()
        if row:
            self.__balance = row[0]
        print(f"== Balance: ₹{self.__balance:.2f}")
