import csv
from datetime import datetime


class Contact:
    class Company:
        def __init__(self):
            self._name = ''
            self._occupation = ''
            self._address = ''
            self._web_page = ''

        def print_company(self):
            print("Company name: ", self._name)
            print("Company occupation: ", self._occupation)
            print("Company address: ", self._address)
            print("Company web page: ", self._web_page)

        @property
        def name(self):
            return self._name

        def set_name(self, name):
            self._name = name

        @property
        def occupation(self):
            return self._occupation

        def set_occupation(self, occupation):
            self._occupation = occupation

        @property
        def address(self):
            return self._address

        def set_address(self, address):
            self._address = address

        @property
        def web_page(self):
            return self._web_page

        def set_web_page(self, web_page):
            self._web_page = web_page

    class OtherPhones:
        def __init__(self):
            self._mobile_phone2 = ''
            self._mobile_phone3 = ''
            self._home_phone = ''
            self._office_phone = ''

        def print_other_phones(self):
            print("Mobile phone 2: ", self._mobile_phone2)
            print("Mobile phone 3: ", self._mobile_phone3)
            print("Home phone: ", self._home_phone)
            print("Office phone: ", self._office_phone)

        @property
        def mobile_phone2(self):
            return self._mobile_phone2

        def set_mobile_phone2(self, mobile_phone2):
            self._mobile_phone2 = mobile_phone2

        @property
        def mobile_phone3(self):
            return self._mobile_phone3

        def set_mobile_phone3(self, mobile_phone3):
            self._mobile_phone3 = mobile_phone3

        @property
        def home_phone(self):
            return self._home_phone

        def set_home_phone(self, home_phone):
            self._home_phone = home_phone

        @property
        def office_phone(self):
            return self._office_phone

        def set_office_phone(self, office_phone):
            self._office_phone = office_phone

    class Emails:
        def __init__(self):
            self._private_email = ''
            self._private_email2 = ''
            self._office_email = ''

        def print_emails(self):
            print("Private email: ", self._private_email)
            print("Private email 2: ", self._private_email2)
            print("Office email: ", self._office_email)

        @property
        def private_email(self):
            return self._private_email

        def set_private_email(self, private_email):
            self._private_email = private_email

        @property
        def private_email2(self):
            return self._private_email2

        def set_private_email2(self, private_email2):
            self._private_email2 = private_email2

        @property
        def office_email(self):
            return self._office_email

        def set_office_email(self, office_email):
            self._office_email = office_email

    class Other:
        class Spouse:
            def __init__(self):
                self._name = ''
                self._birthday = ''
                self._notes = ''

            def print_spouse(self):
                print("Spouse name: ", self._name)
                print("Spouse birthday: ", self._birthday)
                print("Spouse notes: ", self._notes)

            @property
            def name(self):
                return self._name

            def set_name(self, name):
                self._name = name

            @property
            def birthday(self):
                return self._birthday

            def set_birthday(self, birthday):
                self._birthday = birthday

            @property
            def notes(self):
                return self._notes

            def set_notes(self, notes):
                self._notes = notes

        class Children:
            def __init__(self):
                self._name = ''
                self._birthday = ''
                self._notes = ''

            def print_children(self):
                print("Children name: ", self._name)
                print("Children birthday: ", self._birthday)
                print("Children notes: ", self._notes)

            @property
            def name(self):
                return self._name

            def set_name(self, name):
                self._name = name

            @property
            def birthday(self):
                return self._birthday

            def set_birthday(self, birthday):
                self._birthday = birthday

            @property
            def notes(self):
                return self._notes

            def set_notes(self, notes):
                self._notes = notes

        def print_other(self):
            print("Address: ", self._address)
            print("Birthday: ", self._birthday)
            print("Notes: ", self._notes)
            self._spouse.print_spouse()
            self._children.print_children()

        def __init__(self):
            self._address = ''
            self._birthday = ''
            self._notes = ''
            self._spouse = self.Spouse()
            self._children = self.Children()

        @property
        def address(self):
            return self._address

        def set_address(self, address):
            self._address = address

        @property
        def birthday(self):
            return self._birthday

        def set_birthday(self, birthday):
            self._birthday = birthday

        @property
        def notes(self):
            return self._notes

        def set_notes(self, notes):
            self._notes = notes

        @property
        def spouse(self):
            return self._spouse

        @property
        def children(self):
            return self._children

    def __init__(self):
        self._name = ''
        self._mobile_phone = ''
        self._melody = ''
        self._company = self.Company()
        self._other_phones = self.OtherPhones()
        self._emails = self.Emails()
        self._other = self.Other()

    def print_contact(self):
        print('Name: ', self._name)
        print('Mobile phone: ', self._mobile_phone)
        print('Company details: ')
        self._company.print_company()
        print('Other phones: ')
        self._other_phones.print_other_phones()
        print('Emails: ')
        self._emails.print_emails()
        print('Melody: ', self._melody)
        print('Other: ')
        self._other.print_other()

    @property
    def name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    @property
    def mobile_phone(self):
        return self._mobile_phone

    def set_mobile_phone(self, mobile_phone):
        self._mobile_phone = mobile_phone

    @property
    def company(self):
        return self._company

    @property
    def other_phones(self):
        return self._other_phones

    @property
    def emails(self):
        return self._emails

    @property
    def melody(self):
        return self._melody

    def set_melody(self, melody):
        self._melody = melody

    @property
    def other(self):
        return self._other


class Group:
    _contacts = []

    def __init__(self):
        self._name = input("Enter group name: ")
        self._contacts = []

    def search_contact(self, contact_name):
        i = 0
        while i < len(self._contacts):
            if contact_name == contacts[i].name:
                return True
            i = i + 1
        return False

    def add_contact(self, contact):
        if self.search_contact(contact.name):
            return
        self._contacts.append(contact)

    def delete_contact(self, contact):
        i = 0
        while i < len(self._contacts):
            if contact.name == self._contacts[i].name:
                self._contacts.pop(i)
                return
            i = i + 1
        print("Contact was not found!")

    def show_contacts(self):
        i = 0
        print(self._name)
        while i < len(self._contacts):
            self._contacts[i].print_contact()

    @property
    def name(self):
        return self._name

    @property
    def contacts(self):
        return self._contacts


contacts = []
groups = []
melodies = ["nokia tune", "iPhone tune", "huawei tune", "samsung tune", "xiaomi tune"]


def add():
    contact = Contact()
    name = input("Enter name: ")
    contact._name = name
    mobile_phone = input("Enter mobile phone: ")
    contact._mobile_phone = mobile_phone
    print("Available melodies: ")
    for x in melodies:
        print(" - ", x)
    melody_found = False
    while not melody_found:
        melody = input("Enter melody name: ")
        melody_found = False
        for x in melodies:
            if melody == x:
                melody_found = True
                contact._melody = melody
        if not melody_found:
            print("Melody was not found!")
    company_name = input("Enter company name: ")
    contact.company._name = company_name
    company_occupation = input("Enter company occupation: ")
    contact.company._occupation = company_occupation
    company_address = input("Enter company address: ")
    contact.company._address = company_address
    company_web_page = input("Enter company web page: ")
    contact.company._web_page = company_web_page
    mobile_phone2 = input("Enter second mobile phone: ")
    contact.other_phones._mobile_phone2 = mobile_phone2
    mobile_phone3 = input("Enter third mobile phone: ")
    contact.other_phones._mobile_phone3 = mobile_phone3
    home_phone = input("Enter home phone: ")
    contact.other_phones._home_phone = home_phone
    office_phone = input("Enter office phone: ")
    contact.other_phones._office_phone = office_phone
    private_email = input("Enter private email: ")
    contact.emails._private_email = private_email
    private_email2 = input("Enter second private email: ")
    contact.emails._private_email2 = private_email2
    office_email = input("Enter office email: ")
    contact.emails._office_email = office_email
    address = input("Enter address: ")
    contact.other._address = address
    print("Correct format for birthday: YYYY-MM-DD")
    birthday = input("Enter birthday: ")
    contact.other._birthday = birthday
    notes = input("Enter notes: ")
    contact.other._notes = notes
    spouse_name = input("Enter spouse name: ")
    contact.other.spouse._name = spouse_name
    spouse_birthday = input("Enter spouse birthday: ")
    contact.other.spouse._birthday = spouse_birthday
    spouse_notes = input("Enter spouse notes: ")
    contact.other.spouse._notes = spouse_notes
    children_name = input("Enter children name: ")
    contact.other.children._name = children_name
    children_birthday = input("Enter children birthday: ")
    contact.other.children._birthday = children_birthday
    children_notes = input("Enter children notes: ")
    contact.other.children._notes = children_notes
    contacts.append(contact)
    print("==============================")


def update_contact():
    element = input("Which contact do you want to edit? ")
    i = 0
    while i < len(contacts):
        if element == contacts[i].name:
            print("Possible edits: name, mobile_phone, company_name, company_occupation, company_address, " + "\n" +
                  "company_page, mobile_phone2, mobile_phone3, home_phone, office_phone, private_email, " + "\n" +
                  "private_email2, office_email, melody, address, birthday, notes, spouse_name,  " + "\n" +
                  "spouse_birthday, spouse_notes, children_name, children_birthday, children_notes")
            change = input("What do you want to edit? ")
            if change == "name":
                name = input("Enter new value: ")
                contacts[i].set_name(name)
            if change == "mobile_phone":
                mobile_phone = input("Enter new value: ")
                contacts[i].set_mobile_phone(mobile_phone)
            if change == "company_name":
                company_name = input("Enter new value: ")
                contacts[i].company.set_name(company_name)
            if change == "company_occupation":
                company_occupation = input("Enter new value: ")
                contacts[i].company.set_occupation(company_occupation)
            if change == "company_address":
                company_address = input("Enter new value: ")
                contacts[i].company.set_occupation(company_address)
            if change == "company_page":
                company_web_page = input("Enter new value: ")
                contacts[i].company.set_company_web_page(company_web_page)
            if change == "mobile_phone2":
                mobile_phone2 = input("Enter new value: ")
                contacts[i].other_phones.set_mobile_phone2(mobile_phone2)
            if change == "mobile_phone3":
                mobile_phone3 = input("Enter new value: ")
                contacts[i].other_phones.set_mobile_phone3(mobile_phone3)
            if change == "home_phone":
                home_phone = input("Enter new value: ")
                contacts[i].other_phones.set_home_phone(home_phone)
            if change == "office_phone":
                office_phone = input("Enter new value: ")
                contacts[i].other_phones.set_office_phone(office_phone)
            if change == "private_email":
                private_email = input("Enter new value: ")
                contacts[i].emails.set_private_email(private_email)
            if change == "private_email2":
                private_email2 = input("Enter new value: ")
                contacts[i].emails.set_private_email2(private_email2)
            if change == "office_email":
                office_email = input("Enter new value: ")
                contacts[i].emails.set_office_email(office_email)
            if change == "melody":
                melody = input("Enter new value: ")
                contacts[i].set_melody(melody)
            if change == "address":
                address = input("Enter new value: ")
                contacts[i].other.set_address(address)
            if change == "birthday":
                birthday = input("Enter new value: ")
                contacts[i].other.set_birthday(birthday)
            if change == "notes":
                notes = input("Enter new value: ")
                contacts[i].other.set_notes(notes)
            if change == "spouse_name":
                spouse_name = input("Enter new value: ")
                contacts[i].other.spouse.set_name(spouse_name)
            if change == "spouse_birthday":
                spouse_birthday = input("Enter new value: ")
                contacts[i].other.spouse.set_birthday(spouse_birthday)
            if change == "spouse_notes":
                spouse_notes = input("Enter new value: ")
                contacts[i].other.spouse.set_notes(spouse_notes)
            if change == "children_name":
                children_name = input("Enter new value: ")
                contacts[i].other.children.set_name(children_name)
            if change == "children_birthday":
                children_birthday = input("Enter new value: ")
                contacts[i].other.children.set_birthday(children_birthday)
            if change == "children_notes":
                children_notes = input("Enter new value: ")
                contacts[i].other.children.set_notes(children_notes)
            return
        i = i + 1
    print("Contact was not found!")


def show_all_contacts():
    i = 0
    count = len(contacts)
    while i < count:
        print("ID:", i + 1)
        contacts[i].print_contact()
        i = i + 1
        print("")


def delete_contact():
    element = input("Which contact (name) do you want to delete? ")
    i = 0
    while i < len(contacts):
        if element == contacts[i].name:
            contacts.pop(i)
            return
        i = i + 1
    print("Contact was not found!")


def search_contact():
    element = input("Which contact (name) do you search for? ")
    i = 0
    while i < len(contacts):
        if element == contacts[i].name:
            contacts[i].print_contact()
            return contacts[i]
        i = i + 1
    print("Contact was not found!")


def add_group():
    groups.append(Group())


def add_contact_to_group():
    show_all_groups()
    g_index = input('Enter group index: ')
    print("Which contact (name) do you want to add to", groups[int(g_index)].name, end='')
    element = input("? ")

    for i in contacts:

        if element == i.name:
            groups[int(g_index)].add_contact(i)
            return
    print("Contact was not found!")


def delete_group():
    show_all_groups()
    g_index = input('Enter group index: ')
    groups.pop(int(g_index))


def delete_contact_from_group():
    show_all_groups()
    g_index = input('Enter group index: ')
    print("Which contact (name) do you want to delete from", groups[int(g_index)].name, end='')
    element = input("? ")

    for i in contacts:
        if element == i.name:
            groups[int(g_index)].delete_contact(i)
            return
    print("Contact was not found!")


def show_all_groups():
    index = 0
    for i in groups:
        print(index, '-', i.name, ':', end='')
        index += 1
        for j in i.contacts:
            print(j.name, end='')
        print('.\n')


def days_between(d1):
    d1_split = d1.split("-")
    today = datetime.now()
    d1 = str(today.year) + "-" + d1_split[1] + "-" + d1_split[2]
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    return abs((today - d1).days)


def reminder():
    for x in contacts:
        if days_between(x.other.birthday) < 10:
            print(x.name, "has birthday on", x.other.birthday)


def import_csv():
    file_name = input("What is the name of the import file? ")
    with open(file_name, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            i = 0
            contact = Contact()
            contact._name = row[i]
            i = i + 1
            contact._mobile_phone = row[i]
            i = i + 1
            contact._melody = row[i]
            i = i + 1
            contact.company._name = row[i]
            i = i + 1
            contact.company._occupation = row[i]
            i = i + 1
            contact.company._address = row[i]
            i = i + 1
            contact.company._web_page = row[i]
            i = i + 1
            contact.other_phones._mobile_phone2 = row[i]
            i = i + 1
            contact.other_phones._mobile_phone3 = row[i]
            i = i + 1
            contact.other_phones._home_phone = row[i]
            i = i + 1
            contact.other_phones._office_phone = row[i]
            i = i + 1
            contact.emails._private_email = row[i]
            i = i + 1
            contact.emails._private_email2 = row[i]
            i = i + 1
            contact.emails._office_email = row[i]
            i = i + 1
            contact.other._address = row[i]
            i = i + 1
            contact.other._birthday = row[i]
            i = i + 1
            contact.other._notes = row[i]
            i = i + 1
            contact.other.spouse._name = row[i]
            i = i + 1
            contact.other.spouse._birthday = row[i]
            i = i + 1
            contact.other.spouse._notes = row[i]
            i = i + 1
            contact.other.children._name = row[i]
            i = i + 1
            contact.other.children._birthday = row[i]
            i = i + 1
            contact.other.children._notes = row[i]
            contacts.append(contact)


def export_csv():
    file_name = input("What is the name of the export file? ")
    try:
        with open(file_name, 'w') as f:
            writer = csv.writer(f)
            for contact in contacts:
                writer.writerow([contact.name,
                                 contact.mobile_phone,
                                 contact.melody,
                                 contact.company.name,
                                 contact.company.occupation,
                                 contact.company.address,
                                 contact.company.web_page,
                                 contact.other_phones.mobile_phone2,
                                 contact.other_phones.mobile_phone3,
                                 contact.other_phones.home_phone,
                                 contact.other_phones.office_phone,
                                 contact.emails.private_email,
                                 contact.emails.private_email2,
                                 contact.emails.office_email,
                                 contact.other.address,
                                 contact.other.birthday,
                                 contact.other.notes,
                                 contact.other.spouse.name,
                                 contact.other.spouse.birthday,
                                 contact.other.spouse.notes,
                                 contact.other.children.name,
                                 contact.other.children.birthday,
                                 contact.other.children.notes])
    except BaseException as e:
        print('Error while exporting contacts to ', file_name, e)
    else:
        print('Contacts were exported successfully !')


def export_all_text():
    file_name = input("What is the name of the import file? ")
    file = open(file_name, "w")

    for i in contacts:
        string = str(i.name) + "-" + str(i.mobile_phone) + "-" + str(i.melody) + " \n"
        file.write(string)
    file.close()


def export_single_text():
    file_name = input("What is the name of the import file? ")
    file = open(file_name, "w")
    show_all_contacts()
    element = input("What is the name of the contact you want to export? ")

    for i in contacts:
        if element == i.name:
            string = (str(i.name) + "\n" + str(i.mobile_phone) +
                      "\n" + str(i.melody) +
                      "\n" + str(i.company.name) +
                      "\n" + str(i.company.occupation) +
                      "\n" + str(i.company.address) +
                      "\n" + str(i.company.web_page) +
                      "\n" + str(i.other_phones.mobile_phone2) +
                      "\n" + str(i.other_phones.mobile_phone3) +
                      "\n" + str(i.other_phones.home_phone) +
                      "\n" + str(i.other_phones.office_phone) +
                      "\n" + str(i.emails.private_email) +
                      "\n" + str(i.emails.private_email2) +
                      "\n" + str(i.emails.office_email) +
                      "\n" + str(i.other.address) +
                      "\n" + str(i.other.birthday) +
                      "\n" + str(i.other.notes) +
                      "\n" + str(i.other.spouse.name) +
                      "\n" + str(i.other.spouse.birthday) +
                      "\n" + str(i.other.spouse.notes) +
                      "\n" + str(i.other.children.name) +
                      "\n" + str(i.other.children.birthday) +
                      "\n" + str(i.other.children.notes))

            file.write(string)
            return
    print("Contact was not found!")


def show_menu():
    print("1. Add new contact")
    print("2. Update contact")
    print("3. Delete contact")
    print("4. Search contact")
    print("5. Show all contacts")
    print("==============================")
    print("6 Create group")
    print("7. Add contact to group")
    print("8. Delete contact from group")
    print("9. Show all groups")
    print("10. Delete group")
    print("==============================")
    print("11. Import contact")
    print("12. Export contact")
    print("13. Print contact list")
    print("14. Print contact's details")
    print("==============================")
    print("15. Birthday reminder")
    print("16. Exit")
    print("")
    while True:
        try:
            print("")
            choice = int(input("Enter your choice: "))
            print("")

            if 1 <= choice <= 16:
                if choice == 1:
                    add()
                if choice == 2:
                    update_contact()
                if choice == 3:
                    delete_contact()
                if choice == 4:
                    search_contact()
                if choice == 5:
                    show_all_contacts()
                if choice == 6:
                    add_group()
                if choice == 7:
                    add_contact_to_group()
                if choice == 8:
                    delete_contact_from_group()
                if choice == 9:
                    show_all_groups()
                if choice == 10:
                    delete_group()
                if choice == 11:
                    import_csv()
                if choice == 12:
                    export_csv()
                if choice == 13:
                    export_all_text()
                if choice == 14:
                    export_single_text()
                if choice == 15:
                    reminder()
                if choice == 16:
                    break
            else:
                print("Wrong command!")
                print("")
        except ValueError:
            print("Wrong input!")
            print("")


show_menu()
