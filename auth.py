
import json, os
from helpers import validate_email, validate_egyptian_phone

USERS_FILE = "users.json"

def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        # json.dump(users, f)
        json.dump(users, f, indent=2)

def register():
    users = load_users()
    print("\n--- Register ---")
    
    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()
  
    email = input("Email: ").strip()
    if not validate_email(email):
        print("❌ Email is not valid!")
        return None
    if any(u["email"] == email for u in users):
        print("❌ This email is already registered!")
        return None
    
    password = input("Password: ").strip()
    confirm = input("Confirm Password: ").strip()
    if password != confirm:
        print("❌ Passwords do not match!")
        return None
    
    phone = input("Phone Number (Egyptian): ").strip()
    if not validate_egyptian_phone(phone):
        print("❌ Phone number is not valid! It must start with 010/011/012/015")
        return None
    
    user = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "phone": phone
    }
    users.append(user)
    save_users(users)
    print("✅ Registration successful!")
    return user

def login():
    users = load_users()
    print("\n--- Login ---")
    email = input("Email: ").strip()
    password = input("Password: ").strip()
    
    for user in users:
        if user["email"] == email and user["password"] == password:
            print(f"✅ Welcome {user['first_name']}!")
            return user
    
    print("❌ Email or password is incorrect!")
    return None