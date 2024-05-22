import os
from dotenv import load_dotenv

from manager.DataManager import DataManager
from schemas.Contact import NewContact

load_dotenv()
DATABASE = os.getenv("DATABASE")
md = DataManager(DATABASE)
# md.createTables()

# newContact1 = NewContact("firstname", "firstlast")
# newContact2 = NewContact("secondname", "secondlast")
# newContact3 = NewContact("threethname", "threethlast")
#
# md.addNewContact(newContact1)
# md.addNewContact(newContact2)
# md.addNewContact(newContact3)

print(md.getContacts())
