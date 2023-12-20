import json

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class ContactBook:
    def __init__(self):
        self.contacts = {}
        self.load_data()

    def load_data(self):
        try:
            with open('contacts.json', 'r') as file:
                data = json.load(file)
                self.contacts = {int(contact_id): Contact(**contact_info) for contact_id, contact_info in data.items()}
        except FileNotFoundError:
            pass

    def save_data(self):
        with open('contacts.json', 'w') as file:
            json.dump({contact_id: contact.__dict__ for contact_id, contact in self.contacts.items()}, file, indent=2)

    def add_contact(self, name, phone, email):
        contact_id = max(self.contacts.keys(), default=0) + 1
        new_contact = Contact(name, phone, email)
        self.contacts[contact_id] = new_contact
        self.save_data()
        print(f"Contact '{name}' added successfully!")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contacts:")
            for contact_id, contact in self.contacts.items():
                print(f"ID: {contact_id}, {contact}")

    def search_contacts(self, search_term):
        results = [(contact_id, contact) for contact_id, contact in self.contacts.items()
                   if search_term.lower() in contact.name.lower() or search_term.lower() in contact.email.lower()]
        return results

    def delete_contact(self, contact_id):
        if contact_id in self.contacts:
            deleted_contact = self.contacts.pop(contact_id)
            self.save_data()
            print(f"Contact '{deleted_contact.name}' deleted successfully!")
        else:
            print("Contact not found.")

    def update_contact(self, contact_id, name=None, phone=None, email=None):
        if contact_id in self.contacts:
            contact = self.contacts[contact_id]
            if name:
                contact.name = name
            if phone:
                contact.phone = phone
            if email:
                contact.email = email
            self.save_data()
            print(f"Contact '{contact.name}' updated successfully!")
        else:
            print("Contact not found.")

def display_menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contacts")
    print("4. Delete Contact")
    print("5. Update Contact")
    print("6. Quit")

def main():
    contact_book = ContactBook()

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            contact_book.add_contact(name, phone, email)
        elif choice == '2':
            contact_book.display_contacts()
        elif choice == '3':
            search_term = input("Enter search term: ")
            results = contact_book.search_contacts(search_term)
            if results:
                print("Search results:")
                for contact_id, contact in results:
                    print(f"ID: {contact_id}, {contact}")
            else:
                print("No matching contacts found.")
        elif choice == '4':
            contact_id = int(input("Enter the ID of the contact to delete: "))
            contact_book.delete_contact(contact_id)
        elif choice == '5':
            contact_id = int(input("Enter the ID of the contact to update: "))
            name = input("Enter new name (leave blank to keep current): ")
            phone = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email address (leave blank to keep current): ")
            contact_book.update_contact(contact_id, name, phone, email)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
