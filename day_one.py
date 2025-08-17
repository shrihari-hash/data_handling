import csv
import os

FILENAME = "contact.csv"

# Create file with headers if it doesn't exist
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email"])


def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    # Check for duplicates
    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Name"].lower() == name.lower():
                print("Contact name already exists")
                return

    with open(FILENAME, 'a', newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, email])
        print("Contact added")


def view_contact():
    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

        if len(rows) <= 1:
            print("No contact found")
            return

        print("\nYour contacts:")
        print(f"{rows[0][0]} | {rows[0][1]} | {rows[0][2]}")
        print("-" * 40)

        for row in rows[1:]:
            print(f"{row[0]} | {row[1]} | {row[2]}")
        print()


def search_contact():
    term = input("Enter the name: ").strip().lower()
    found = False

    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if term in row["Name"].lower():
                print(f"{row['Name']} | {row['Phone']} | {row['Email']}")
                found = True

    if not found:
        print("No matching contact found")


def main():
    while True:
        print("\n1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("Thanks for using the contact book!")
            break
        else:
            print("Invalid choice. Please select 1–4.")


if __name__ == "__main__":
    main()

   
