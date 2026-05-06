#Given
phonebook = {
    "AMIT" : "9876543210",
    "RIYA" : "9123456780"
}

print(phonebook)

#Adding contact to phone book
def add_contact():
    name = input("Enter name: ").upper()
    
    if name in phonebook:
        print("Contact already exists! Duplicate not allowed.")
    else:
        number = input("Enter phone number: ")
        phonebook[name] = number
        print("Contact added successfully!")
    

#Searching contact in the phone book
def search_contact():
    search = input("Enter name to search:").upper()
    found = False
    for name, number in phonebook.items():
        if search in name:      #partial search
            print(f"{name} : {number}")
            found = True
        if not found:
            print("Contact not found.")
        
           
#Deleting a contact
def delete_contact():
    name = input("Enter name to delete: ").upper()
    if name in phonebook:
        del phonebook[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")
    
#main function      
while True:
    print("\n----PHONEBOOK MENU----")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try Again.")
        
#Displaying the phonebook       
print("\n----Phonebook----")
for name, number in phonebook.items():
    print(f"{name} : {number}")

    