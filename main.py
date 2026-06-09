

from auth import register, login
from projects import create_project, view_all_projects, edit_project, delete_project, search_by_date

current_user = None

def main():
    global current_user
    while True:
        if not current_user:
            print("\n===== Crowd-Funding App =====")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Choose: ").strip()
            if choice == "1":
                register()
            elif choice == "2":
                current_user = login()
            elif choice == "3":
                print("Goodbye!")
                break
        else:
            print(f"\n===== Welcome {current_user['first_name']} =====")
            print("1. Create Project")
            print("2. View All Projects")
            print("3. Edit My Project")
            print("4. Delete My Project")
            print("5. Search by Date")
            print("6. Logout")
            choice = input("Choose: ").strip()
            if choice == "1":
                create_project(current_user)
            elif choice == "2":
                view_all_projects()
            elif choice == "3":
                edit_project(current_user)
            elif choice == "4":
                delete_project(current_user)
            elif choice == "5":
                search_by_date()
            elif choice == "6":
                current_user = None

if __name__ == "__main__":
    main()