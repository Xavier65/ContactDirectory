import os
from dotenv import load_dotenv

from manager.DataManager import DataManager
from schemas.Contact import NewContact
from schemas.Address import NewAddress
from schemas.CellphoneNumber import NewCellphoneNumber

load_dotenv()
DATABASE = os.getenv("DATABASE")
md = DataManager(DATABASE)
md.createTables()

newContact1 = NewContact("firstname", "firstlast")
newAddress1 = NewAddress(1, "Wall Street 21th")
newCellphoneNumber1 = NewCellphoneNumber(1, "+504 3389 9873")
newContact2 = NewContact("secondname", "secondlast")
newAddress2 = NewAddress(2, "Main Street 19th")
newCellphoneNumber2 = NewCellphoneNumber(2, "+502 8123 8234")
newContact3 = NewContact("threethname", "threethlast")
newAddress3 = NewAddress(3, "Jornell Street 2th")
newCellphoneNumber3 = NewCellphoneNumber(3, "+501 9234 8923")

md.addNewContact(newContact1)
md.addNewAddress(newAddress1)
md.addNewCellphoneNumber(newCellphoneNumber1)

md.addNewContact(newContact2)
md.addNewAddress(newAddress2)
md.addNewCellphoneNumber(newCellphoneNumber2)

md.addNewContact(newContact3)
md.addNewAddress(newAddress3)
md.addNewCellphoneNumber(newCellphoneNumber3)


print(md.getAllContacts())
