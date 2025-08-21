from db_connection import get_connection

class Banker:
    def __init__(self, banker_id=None, name=None, email=None, phone=None, password=None):
        self.banker_id = banker_id
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password

    def register(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO banker (name, email, phone, password) VALUES (%s,%s,%s,%s)",
                    (self.name, self.email, self.phone, self.password))
        conn.commit()
        print("  Banker registered successfully")
        conn.close()

    def login(self, email, password):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT banker_id, name FROM banker WHERE email=%s AND password=%s",
                    (email, password))
        user = cur.fetchone()
        conn.close()
        return user

    def view_customers(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT customer_id, name, email, phone, balance FROM customer")
        rows = cur.fetchall()
        conn.close()
        print("---- All Customers ----")
        for r in rows:
           cid, name, email, phone, balance = r
           print(f"ID: {cid}, Name: {name}, Email: {email}, Phone: {phone}, Balance: ₹{float(balance):.2f}")


    def update_customer(self, customer_id, new_name, new_email, new_phone):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("UPDATE customer SET name=%s, email=%s, phone=%s WHERE customer_id=%s",
                    (new_name, new_email, new_phone, customer_id))
        conn.commit()
        conn.close()
        print("  Customer updated")

    def delete_customer(self, customer_id):
        confirm = input("Are you sure to delete this customer? (Y/N): ")
        if confirm.upper() == "Y":
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("DELETE FROM customer WHERE customer_id=%s", (customer_id,))
            conn.commit()
            conn.close()
            print("  Customer deleted")
        else:
            print("  Deletion cancelled")
