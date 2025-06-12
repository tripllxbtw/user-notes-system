# User system with per-user notes and persistent storage

users = {}

# -------------------- Load users from file --------------------
def load_users():
    try:
        with open("users.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(":")
                users[username] = password
    except FileNotFoundError:
        pass

# -------------------- Register new user --------------------
def register_user():
    print("\n[REGISTRATION]")
    while True:
        username = input("Create a username: ")
        if username in users:
            print("Username already exists. Try another.")
            continue
        password = input("Create a password: ")
        users[username] = password
        with open("users.txt", "a") as file:
            file.write(f"{username}:{password}\n")
        print(f"User '{username}' registered successfully!")
        return username

# -------------------- Login existing user --------------------
def login_user():
    print("\n[LOGIN]")
    while True:
        username = input("Enter your username: ")
        if username not in users:
            print("User not found. Try again or register.")
            continue
        password = input("Enter your password: ")
        if users[username] == password:
            print(f"Welcome, {username}!")
            return username
        else:
            print("Incorrect password. Try again.")

# -------------------- Notes system --------------------
def notes_menu(username):
    filename = f"notes_{username}.txt"
    while True:
        print("\n[NOTES MENU]")
        choice = input("Enter 'add', 'view', 'change', or 'exit': ").strip().lower()

        if choice == "add":
            note = input("Enter your note: ")
            with open(filename, "a") as f:
                f.write(note + "\n")
            print("Note added.")

        elif choice == "view":
            try:
                with open(filename, "r") as f:
                    lines = f.readlines()
                    if lines:
                        print("\nYour Notes:")
                        for i, line in enumerate(lines, 1):
                            print(f"{i}. {line.strip()}")
                    else:
                        print("No notes found.")
            except FileNotFoundError:
                print("No notes yet.")

        elif choice == "change":
            try:
                with open(filename, "r") as f:
                    lines = f.readlines()
                if not lines:
                    print("No notes to change.")
                    continue
                for i, line in enumerate(lines, 1):
                    print(f"{i}. {line.strip()}")
                index = int(input("Enter number of note to change: ")) - 1
                if 0 <= index < len(lines):
                    new_note = input("Enter new note: ")
                    lines[index] = new_note + "\n"
                    with open(filename, "w") as f:
                        f.writelines(lines)
                    print("Note updated.")
                else:
                    print("Invalid number.")
            except FileNotFoundError:
                print("No notes found.")

        elif choice == "exit":
            print("Logging out. Bye!")
            break

        else:
            print("Invalid choice. Try again.")

# -------------------- Start --------------------

def main():
    load_users()
    print("Welcome to the User System with Personal Notes!")
    while True:
        action = input("Do you want to 'login' or 'register'? (or 'exit'): ").strip().lower()
        if action == 'login':
            username = login_user()
            notes_menu(username)
        elif action == 'register':
            username = register_user()
            notes_menu(username)
        elif action == 'exit':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main()
# -------------------- End of code --------------------