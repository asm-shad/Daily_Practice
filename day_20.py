"""
Challenge: Offline Credential Manager

Create a CLI tool to manage login credentials (website, username, password) in an encoded local file (`vault.txt`).

Your program should:
1. Add new credentials (website, username, password)
2. Automatically rate password strength (weak/medium/strong)
3. Encode the saved content using Base64 for simple offline obfuscation
4. View all saved credentials (decoding them)
5. Update password for any existing website entry (assignment)

Bonus:
- Support searching for a website entry
- Mask password when showing in the list
"""

import base64
import os

VAULT_FILE = "vault.txt"

def encode(text):
    return base64.b64encode(text.encode()).decode()  ## used decode because it's just coverting into regular srting

def decode(text):
    return base64.b64decode(text.encode()).decode()

def password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*().,<>" for c in password)

    score = sum([length >= 8, has_upper, has_digit, has_special])
    return ["Weak", "Medium", "Strong", "Very Strong"][min(score, 3)]

def add_credential():
    website = input("Website: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    strength = password_strength(password)

    line = f"{website}||{username}||{password}"
    encoded_line = encode(line)

    with open(VAULT_FILE, 'a', encoding="utf-8") as f:
        f.write(encoded_line + "\n")

    print("✅ Credential saved")

def view_credentials():
    if not os.path.exists(VAULT_FILE):
        print("File not found")
        return
    
    with open(VAULT_FILE, 'r', encoding="utf-8") as f:
        for line in f:
            decoded = decode(line.strip())
            website, username, password = decoded.split("||")
            hidden_password = '*' * len(password)
            print(f"{website} | {username} | {password}")


def update_password():
    if not os.path.exists(VAULT_FILE):
        print("File not found")
        return

    target_website = input("Enter website to update: ").strip()

    updated_lines = []
    found = False

    with open(VAULT_FILE, 'r', encoding="utf-8") as f:
        for line in f:
            decoded = decode(line.strip())
            website, username, password = decoded.split("||")

            if website.lower() == target_website.lower():
                found = True

                new_password = input("Enter new password: ").strip()

                strength = password_strength(new_password)
                print(f"Password strength: {strength}")

                updated_data = f"{website}||{username}||{new_password}"
                updated_lines.append(encode(updated_data))

            else:
                updated_lines.append(line.strip())

    if found:
        with open(VAULT_FILE, 'w', encoding="utf-8") as f:
            for item in updated_lines:
                f.write(item + "\n")

        print("✅ Password updated successfully")

    else:
        print("❌ Website not found")

def main():
    while True:
        print("\n🔒 Credential Manager")
        print("1. Add credential")
        print("2. View credentials")
        print("3. Update password")
        print("4. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1": add_credential()
            case "2": view_credentials()
            case "4": break
            case _: print("Invalid choice")

if __name__ == "__main__":
    main()