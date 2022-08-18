import json


CONTACT_FILE_PATH = "contact.json"


def read_contacts(file_path):
    try:
        with open(file_path, 'r') as f:
            contacts = json.load(f)['contacts']
    except FileNotFoundError:
        contacts = []

    return contacts


def write_contacts(file_path, contacts):
    with open(file_path, 'w') as f:
        contacts = {"contacts": contacts}
        json.dump(contacts, f)


def verify_email_address(email):
    if "@" not in email:
        return False

    split_email = email.split("@")
    identifier = "".join(split_email[:-1])
    domain = split_email[-1]

    if len(identifier) < 1:
        return False

    if "." not in domain:
        return False

    split_domain = domain.split(".")

    for section in split_domain:
        if len(section) == 0:
            return False

    return True


def add_contact(contacts):
    first = input("First Name: ")
    while first == "":
        print("Contact must have first name.")
        first = input("First Name: ")
    last = input("Last Name: ")
    while last == "":
        print("Contact must have last name.")
        last = input("Last Name: ")
    mobile = input("Mobile Phone Number: ")
    home = input("Home Phone Number: ")
    email = input("Email Address: ")
    address = input("Address: ")
    for i in contacts:
        if first == i["first_name"] and last == i["last_name"]:
            print("A contact with this name already exists.")
            return "You entered invalid information, this contact was not added."
    counter = 0
    for i in mobile:
        if i.isdigit():
            counter += 1
    if not (counter == 10 or counter == 0):
        print("Invalid mobile phone number.")
        return "You entered invalid information, this contact was not added."
    home_counter = 0
    for i in home:
        if i.isdigit():
            home_counter += 1
    if not (home_counter == 10 or home_counter == 0):
        print("Invalid home phone number.")
        return "You entered invalid information, this contact was not added"
    if email == "":
        pass
    elif verify_email_address(email) == False:
        print("Invalid email address.")
        return "You entered invalid information, this contact was not added"

    dic = {"first_name": first, "last_name": last, "mobile": mobile,
           "home": home, "email": email, "address": address}

    contacts.append(dic)
    return ""


def search_for_contact(contacts):
    first = input("First Name: ")
    last = input("Last Name: ")
    matches = []
    for j, i in enumerate(contacts):
        p_first = i["first_name"]
        p_last = i["last_name"]
        if first in p_first and last in p_last:
            matches.append(j)
    num_matches = len(matches)
    print(f"Found {num_matches} matching contacts.")
    mat_dis = []
    for i in matches:
        mat_dis.append(contacts[i])

    num = 1
    for i in mat_dis:
        first = i["first_name"]
        last = i["last_name"]
        mobile = i["mobile"]
        home = i["home"]
        email = i["email"]
        address = i["address"]
        print(f"{num}. {first} {last}")
        if not mobile == "":
            print(f"        Mobile: {mobile}")
        if not home == "":
            print(f"        Home: {home}")
        if not email == "":
            print(f"        Email: {email}")
        if not address == "":
            print(f"        Address: {address}")
        num += 1


def delete_contact(contacts):
    first = input("First Name: ")
    last = input("Last Name: ")
    for j, i in enumerate(contacts):
        if i["first_name"] == first and i["last_name"] == last:
            answer = input("Are you sure you would like to delete this contact (y/n)? ")
            if answer == "y":
                contacts.pop(j)
                return ""
        else:
            continue
    print("No contact found")


def list_contacts(contacts):
    num = 1
    for i in contacts:
        first = i["first_name"]
        last = i["last_name"]
        mobile = i["mobile"]
        home = i["home"]
        email = i["email"]
        address = i["address"]
        print(f"{num}. {first} {last}")
        if not mobile == "":
            print(f"        Mobile: {mobile}")
        if not home == "":
            print(f"        Home: {home}")
        if not email == "":
            print(f"        Email: {email}")
        if not address == "":
            print(f"        Address: {address}")
        num += 1


def main(contacts_path):

    con = read_contacts(contacts_path)

    print("""Welcome to your contact list!
    The following is a list of useable commands:
    \"add\": Adds a contact.
    \"delete\": Deletes a contact.
    \"list\": Lists all contacts.
    \"search\": Searches for a contact by name.
    \"q\": Quits the program and saves the contact list.\n""")

    command = input("Type a command: ")
    while not command == "q":
        if command == "add":
            print(add_contact(con))
        elif command == "delete":
            delete_contact(con)
        elif command == "list":
            list_contacts(con)
        elif command == "search":
            search_for_contact(con)
        command = input("Type a command: ")

    write_contacts(CONTACT_FILE_PATH, con)
    print("Contacts were saved successfully.")


if __name__ == "__main__":
    main(CONTACT_FILE_PATH)
