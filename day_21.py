"""
 Challenge: Offline Notes Locker

Create a terminal-based app that allows users to save, view, and search personal notes securely in an encrypted file.

Your program should:
1. Let users add notes with title and content.
2. Automatically encrypt each note using Fernet (AES under the hood).
3. Store all encrypted notes in a single `.vault` file (JSON format).
4. Allow listing of titles and viewing/decrypting selected notes.
5. Support searching by title or keyword.

Bonus:
- Add timestamps to notes.
- Use a master password to unlock vault (optional).
"""

import json
import os
from cryptography.fernet import Fernet
from datetime import datetime

VAULT_FILE = "notes_vault.json"
KEY_FILE = "vault.key"

def load_or_create_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:  ## write a binary file
            f.write(key) 
    else:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
    
    return Fernet(key)

fernet = load_or_create_key()

def load_vault():
    if not os.path.exists(VAULT_FILE):
        return []
    with open(VAULT_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def save_vault(data):
    with open(VAULT_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def add_note():
    title = input("Enter note title: ").strip()
    content = input("Enter note content: ").strip()

    encrypted_content = fernet.encrypt(content.encode()).decode()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = load_vault()
    data.append({
        "title": title,
        "content": encrypted_content,
        "timestamp": timestamp
    })

    save_vault(data)
    print("Note added successfully!")
    
def list_notes():
    data = load_vault()
    if not data:
        print("No notes yet.")
        return
    
    for i, note in enumerate(data, 1):
        print(f"{i}. {note['title']} {note['timestamp']}")
        
def view_note():
    list_notes()
    try:
        idx = int(input("Enter note number to view: ")) -1
        data = load_vault()
        if 0 <= idx <= len(data):
            encrypted_content = data[idx]["content"]
            decrypted = fernet.decrypt(encrypted_content.encode()).decode()
            print(f"\n {data[idx]["title"]} - {data[idx]["timestamp"]} \n\n {decrypted}")
        else:
            print("Invalid Selection")
    except:
        print("Invalid Input")

def search_notes():
    data = load_vault()

    if not data:
        print("No notes found.")
        return

    key = input("Enter title or keyword to search: ").strip().lower()

    found = False

    for note in data:
        title = note["title"]

        # decrypt content for searching
        decrypted_content = fernet.decrypt(
            note["content"].encode()
        ).decode()

        # search in title OR content
        if (
            key in title.lower()
            or key in decrypted_content.lower()
        ):
            found = True

            print("\n--------------------")
            print(f"Title: {title}")
            print(f"Time : {note['timestamp']}")
            print(f"Content:\n{decrypted_content}")
            print("--------------------")

    if not found:
        print("No matching notes found.")

def main():
    while True:
        print("\n🔐 Offline Notes Locker")
        print("1. Add Note")
        print("2. List Notes")
        print("3. View Note")
        print("4. Search Notes")
        print("5. Exit")

        choice = input("Enter an option: ").strip()

        match choice:
            case "1": add_note()
            case "2": list_notes()
            case "3": view_note()
            case "4": search_notes()
            case "5": break
            case _: print("Invalid input")

if __name__ == "__main__":
    main()