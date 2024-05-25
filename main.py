import os
from dotenv import load_dotenv

from manager.DataManager import DataManager
from schemas.Contact import NewContact
from schemas.Address import NewAddress
from schemas.CellphoneNumber import NewCellphoneNumber

load_dotenv()
DATABASE = os.getenv("DATABASE")
md = DataManager(DATABASE)
# md.createTables()

contact = [
    NewContact({"firstname": "Juan", "lastname": "Perez"}),
    NewContact({"firstname": "Benito", "lastname": "Paredez"}),
    NewContact({"firstname": "Marcos", "lastname": "Marquez"}),
]
address = [
    NewAddress({"contact_id": 1, "address": "Wall Street 21th"}),
    NewAddress({"contact_id": 2, "address": "Main Street 19th"}),
    NewAddress({"contact_id": 3, "address": "Jornell Street 2th"}),
]
numbers = [
    NewCellphoneNumber({"contact_id": 1, "cellphone_number": "+504 3389 9873"}),
    NewCellphoneNumber({"contact_id": 2, "cellphone_number": "+502 8123 8234"}),
    NewCellphoneNumber({"contact_id": 3, "cellphone_number": "+501 9234 8923"}),
]

# for item in range(3):
#    md.addNewContact(contact[item], address[item], numbers[item])

# print(f"Result All Contactos: {md.getAllContacts()}")
# print(f"Result Contact Number: {md.getContactNumber("33")}")
# print(f"Result Contact Address: {md.getContactAddress("21th")}")
