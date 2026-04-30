'''
Create a terminal-based contact book tool that stores and manages contacts using a CSV file

Your Program should:
1. Ask the user to choose one of the following options:
    - Add a new contact
    - View all contacts
    - Search for a contact by name
    - Exit
2. Store contacts in a file called `contacts.csv` with columns:
    - Name
    - Phone
    - Email
3. If the file doesn't exist, create it autometically
4. Keep the interfacr clean and clear

'''

import csv
import os

FILENAME = "contacts.csv"

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email"])

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    # check for duplicates
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Name"].lower() == name.lower():
                print("Contact name already exists.")
                return 
            
    with open(FILENAME, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, email])
        print("Contact Added.")

def view_contacts():
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

        if len(rows) < 1:
            print("No contacts found")
            return

        print("\n Your contacts: \n")

        for row in rows[1:]:
            print(f"{row[0]} | {row[1]} | {row[2]}")
        print()

def search_contact():
    term = input("Enter the name to search: ").strip().lower()
    found = False

    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if term in row["Name"].lower():
                print(f"{row['Name']} | {row['Phone']} | {row['Email']}")
                found = True

    if not found:
        print("No matching contact found.")

def main():
    while True:
        print("\n Contact Book")
        print("1. Add Contact")
        print("2. View all contacts")
        print("3. Search for a contact")
        print("4. Exit")

        choice = input("Choose an option (1-4)").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("Thanks for using our software")
            break
        else:
            print("Invalid Choice of number.")


if __name__ == "__main__":
    main()