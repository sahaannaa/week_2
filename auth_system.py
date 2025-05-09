import hashlib

# Dictionary to store user credentials
user_db = {}

def hash_password(password):
    """Hash a password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    if username in user_db:
        print("User already exists.")
    else:
        hashed_pw = hash_password(password)
        user_db[username] = hashed_pw
        print("Created new user")

def login(username, password):
    hashed_pw = hash_password(password)
    stored_pw = user_db.get(username)

    if stored_pw is None:
        print("User not found")
    elif hashed_pw == stored_pw:
        print("Login Successful")
    else:
        print("Incorrect password")

if __name__ == "__main__":
    while True:
        choice = input("\nChoose an option: register / login / exit: ").strip().lower()
        if choice == "register":
            u = input("Enter username: ")
            p = input("Enter password: ")
            register(u, p)
        elif choice == "login":
            u = input("Enter username: ")
            p = input("Enter password: ")
            login(u, p)
        elif choice == "exit":
            print("Exiting program.")
            break
        else:
            print("Invalid option.")

