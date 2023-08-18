import sqlite3
import bcrypt
import string
import random
import pyfiglet

# Database connection and cursor
conn = sqlite3.connect("passwords.db")
cursor = conn.cursor()

# Create a table to store passwords if it doesn't exist already
cursor.execute("""
    CREATE TABLE IF NOT EXISTS passwords (
        website TEXT PRIMARY KEY,
        username TEXT,
        password TEXT
    )
""")
conn.commit()


def add_password():
    while True:
        website = input("Enter the website or service name: ")
        # Use a context manager to handle transactions and connection
        with conn:
            cursor.execute("SELECT 1 FROM passwords WHERE website=?", (website,))
            exists = cursor.fetchone()
            if exists:
                print("Website already exists in the database.")
                continue

            username = input("Enter your username: ")
            password = input("Enter your password: ")

            # Hash the password using bcrypt before storing
            hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

            cursor.execute("""
                INSERT INTO passwords (website, username, password)
                VALUES (?, ?, ?)
            """, (website, username, hashed_password))
            print(f"Password for {website} added successfully.")
            break


def retrieve_password():
    website = input("Enter the website or service name: ")

    with conn:
        cursor.execute("SELECT password FROM passwords WHERE website=?", (website,))
        result = cursor.fetchone()

        if result:
            hashed_password = result[0].encode()
            original_password = input("Enter your master password: ").encode()

            if bcrypt.checkpw(original_password, hashed_password):
                print("Access granted. The password is:", hashed_password.decode())
            else:
                print("Access denied. Incorrect master password.")
        else:
            print(f"Password for {website} not found.")


def update_password():
    """Update a password for a website in the Password Manager."""
    website = input("Enter the website or service name: ")

    with conn:
        exists = cursor.execute("SELECT 1 FROM passwords WHERE website=? AND password IS NOT NULL", (website,)).fetchone()
        if exists is None:
            print(f"Password for {website} not found.")
            return

        old_password = input("Enter the old password: ")
        new_password = input("Enter the new password: ")

        # Hash the old and new passwords using bcrypt
        hashed_old_password = bcrypt.hashpw(old_password.encode(), bcrypt.gensalt()).decode()
        hashed_new_password = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()

        cursor.execute("""
            UPDATE passwords
            SET password = ?
            WHERE website = ? AND password = ?
        """, (hashed_new_password, website, hashed_old_password))
        print(f"Password for {website} updated successfully.")


def delete_password():
    """Delete a password for a website from the Password Manager."""
    website = input("Enter the website or service name: ")

    cursor.execute("DELETE FROM passwords WHERE website=?", (website,))
    conn.commit()
    print(f"Password for {website} deleted successfully.")


def show_all_passwords():
    """Show all passwords stored in the Password Manager."""
    cursor.execute("SELECT website, username FROM passwords")
    result = cursor.fetchall()

    if result:
        print("Stored Passwords:")
        for website, username in result:
            print(f"Website: {website}, Username: {username}")
    else:
        print("No passwords stored yet.")


def generate_password(length=12):
    """Generate a random password and display it."""
    while True:
        password = generate_random_string(length)
        if is_valid_password(password):
            print_password(password)
            break


def generate_random_string(length):
    """Generates a random string of characters.

    Args:
        length (int): The length of the string to generate.

    Returns:
        str: A random string of characters.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def is_valid_password(password):
    """Checks if a string is a valid password.

    Args:
        password (str): The string to check.

    Returns:
        bool: True if the string is a valid password, False otherwise.
    """
    criteria = [
        len(password) >= 8,
        any(c.isupper() for c in password),
        any(c.islower() for c in password),
        any(c.isdigit() for c in password),
        any(c in string.punctuation for c in password),
    ]
    return all(criteria)


def print_password(password):
    """Prints a generated password.

    Args:
        password (str): The password to print.
    """
    print(f"Your password is: {password}")


def main():
    """Main function to manage the Password Manager."""
    # Display ASCII art header using pyfiglet
    header = pyfiglet.figlet_format("Password Manager", font="slant")
    print(header)
    
    while True:
        print("\nPassword Manager Menu:")
        print("1. Add Password")
        print("2. Retrieve Password")
        print("3. Update Password")
        print("4. Delete Password")
        print("5. Show All Passwords")
        print("6. Generate Password")
        print("7. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            retrieve_password()
        elif choice == "3":
            update_password()
        elif choice == "4":
            delete_password()
        elif choice == "5":
            show_all_passwords()
        elif choice == "6":
            generate_password()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
