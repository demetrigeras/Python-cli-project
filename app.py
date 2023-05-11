from peewee import *

db = PostgresqlDatabase('contacts', user='banana', password='123',
                        host='localhost', port=5432)

db.connect()

class BaseModel(Model): 
    class Meta:
        database = db

class Contacts(BaseModel):
    name = CharField()
    email = CharField()
    phone_number = BigIntegerField()


guess = int(input("1: Add Contact\n2: View Contacts\n3: Search contacts by name\nSelect One: "))

def contactselect(guess):
    if guess == 1:
        name = input("Enter the contact's name: ")
        email = input("Enter the contact's email address: ")
        phone_number = int(input("Enter the contact's phone number: "))

        new_contact = Contacts(name=name, email=email, phone_number=phone_number)
        new_contact.save()
    elif guess == 2:
        contacts = Contacts.select()
        for contact in contacts:
            print(contact.name, contact.email, contact.phone_number)

    else: 
        search = input("select a name of a contact: ")
        contacts = Contacts.select().where(Contacts.name == search)
        for contact in contacts:
            print(contact.name, contact.email, contact.phone_number)

        



contactselect(guess)





         # # name, email, phone_number =input("Enter name, email, number: ").split(",") 
        # sql_contacts = name, email, phone_number=input("Enter name, email, number: ").split(",")
        # sql = "INSERT INTO contact"(name, email, phone_number)

        # print("Enter name:",name)
        # print("Enter name:",email)
        # print("Enter name:",phone_number)

        # Create a new contact record and save it to the database

        #     elif guess == 2:
#             print("you kinda did it")
#          else:
#             print("you didn't do it")  


        