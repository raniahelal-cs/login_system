
users = {}

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    confirm = input("Confirm password: ")

    if password != confirm:
        print("Passwords do not match!")
        return
    elif username in users:
        print("User already exists!")
        return
    else:
        users[username] = password
        print("Registration successful!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password")
        print("Please try again")

def change_password():
    username = input("Enter username: ")
    old_password = input("Enter old password: ")
    if username in users and users[username] == old_password:
        new_password = input("Enter new password: ")
        confirm = input("Confirm new password: ")
        if new_password != confirm:
            print("Passwords do not match!")
            return
        
        users[username] = new_password
        print("Password changed successfully!")
    else:
        print("Password change failed!")
        print("Please try again")


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
        print("Invalid choice، Please try again")