import sqlite3

conn = sqlite3.connect("users.db")
cur = conn.cursor()

cur.execute("""
               CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT UNIQUE,
                   password TEXT NOT NULL
               )
           """)

conn.commit()

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    confirm = input("Confirm password: ")

    if password != confirm:
        print("Passwords do not match!")
        return
    
    cur.execute("SELECT * FROM users WHERE username = ?", (username,))
    if cur.fetchone():
        print("User already exists!")
        return
    
    cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    print("Registration successful!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cur.fetchone()
    if user:
        print("Login successful!")
    else:
        print("Invalid username or password")
        print("Please try again")


def change_password():
    username = input("Enter username: ")
    old_password = input("Enter old password: ")
    
    cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, old_password))
    user = cur.fetchone()

    if user:
        new_password = input("Enter new password: ")
        confirm = input("Confirm new password: ")

        if new_password != confirm:
            print("Passwords do not match!")
            return
        
        cur.execute("UPDATE users SET password = ? WHERE username = ?", (new_password, username))
        conn.commit()
        print("Password changed successfully!")
    else:
        print("User not found or incorrect password")

while True:
    print("1. Register")
    print("2. Login")
    print("3. Change Password")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        change_password()
    elif choice == '4':
        print("see you later")
        break
    else:
        print("Invalid choice ,Please try again")
conn.close()