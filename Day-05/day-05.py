# Contact Book System

contacts = {}

def add_contact():
    name = input("Enter contact name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    if name in contacts:
        print(f"{name} already exists in the contact book.")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }

    print(f"{name} added successfully.")


def search_contact():
    name = input("Enter name to search: ").strip()

    if name in contacts:
        print("\nContact found:")
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
        print(f"Address: {contacts[name]['address']}")
    else:
        print("Contact not found.")


def update_contact():
    name = input("Enter the name to update: ").strip()

    if name not in contacts:
        print("Contact not found.")
        return

    print("Leave blank if you do not want to change a field.")

    new_phone = input("New phone number: ").strip()
    new_email = input("New email: ").strip()
    new_address = input("New address: ").strip()

    if new_phone:
        contacts[name]["phone"] = new_phone
    if new_email:
        contacts[name]["email"] = new_email
    if new_address:
        contacts[name]["address"] = new_address

    print(f"{name} updated successfully.")


def delete_contact():
    name = input("Enter the name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print(f"{name} deleted successfully.")
    else:
        print("Contact not found.")


def view_all_contacts():
    if not contacts:
        print("No contacts available.")
        return

    print("\nAll contacts:")
    for name, info in contacts.items():
        print(f"\nName: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        print(f"Address: {info['address']}")


def menu():
    while True:
        print("\n=== Contact Book Menu ===")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            view_all_contacts()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


menu()
