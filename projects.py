
import json, os
from helpers import validate_date

PROJECTS_FILE = "projects.json"

def load_projects():
    if not os.path.exists(PROJECTS_FILE):
        return []
    with open(PROJECTS_FILE, "r") as f:
        return json.load(f)

def save_projects(projects):
    with open(PROJECTS_FILE, "w") as f:
        # json.dump(projects, f)
        json.dump(projects, f, indent=2, ensure_ascii=False)

def create_project(current_user):
    projects = load_projects()
    print("\n--- Create New Project ---")
    
    title = input("Project Title: ").strip()
    details = input("Project Details: ").strip()
    
    try:
        target = float(input("Target Amount (EGP): "))
    except ValueError:
        print("❌ Invalid amount!")
        return
    
    start_date = input("Start Date (YYYY-MM-DD): ").strip()
    if not validate_date(start_date):
        print("❌ Invalid start date!")
        return
    
    end_date = input("End Date (YYYY-MM-DD): ").strip()
    if not validate_date(end_date):
        print("❌ Invalid end date!")
        return
    
    if end_date <= start_date:
        print("❌ End date must be after the start date!")
        return

    project = {
        "id": len(projects) + 1,
        "title": title,
        "details": details,
        "target": target,
        "start_date": start_date,
        "end_date": end_date,
        "owner_email": current_user["email"]
    }
    projects.append(project)
    save_projects(projects)
    print("✅ Project created successfully!")

def view_all_projects():
    projects = load_projects()
    if not projects:
        print("⚠️ No projects available.")
        return
    print("\n--- All Projects ---")
    for p in projects:
        print(f"\n🔹 [{p['id']}] {p['title']}")
        print(f"   Details: {p['details']}")
        print(f"   Target: {p['target']} EGP")
        print(f"   From {p['start_date']} to {p['end_date']}")

def edit_project(current_user):
    projects = load_projects()
    view_all_projects()
    try:
        pid = int(input("\nInput the project ID you want to edit: "))
    except ValueError:
        print("❌ Invalid project ID!")
        return

    for p in projects:
        if p["id"] == pid:
            if p["owner_email"] != current_user["email"]:
                print("❌You are not the owner of this project!")
                return
            p["title"] = input(f"New Title ({p['title']}): ").strip() or p["title"]
            p["details"] = input(f"New Details ({p['details']}): ").strip() or p["details"]
            save_projects(projects)
            print("✅ Project edited successfully!")
            return
    print("❌ Project not found!")

def delete_project(current_user):
    projects = load_projects()
    view_all_projects()
    try:
        pid = int(input("\nInput the project ID you want to delete: "))
    except ValueError:
        print("❌ Invalid project ID!")
        return

    for p in projects:
        if p["id"] == pid:
            if p["owner_email"] != current_user["email"]:
                print("❌ You are not the owner of this project!")
                return
            projects.remove(p)
            save_projects(projects)
            print("✅ Project deleted successfully!")
            return
    print("❌ Project not found!")

def search_by_date():
    projects = load_projects()
    date = input("Input the date to search (YYYY-MM-DD): ").strip()
    results = [p for p in projects if p["start_date"] <= date <= p["end_date"]]
    if results:
        for p in results:
            print(f"\n🔹 {p['title']} | From {p['start_date']} to {p['end_date']}")
    else:
        print("⚠️ No results found.")