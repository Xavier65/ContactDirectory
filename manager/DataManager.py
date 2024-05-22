import sqlite3

from schemas.Contact import Contact, NewContact
from schemas.CellphoneNumber import CellphoneNumber
from schemas.Address import Address


class DataManager:
    def __init__(self, database: str) -> None:
        self.__dbname: str = database

    def __getRows(self, sql_query_sentences: str) -> sqlite3.Cursor | None:
        try:
            conn = sqlite3.connect(self.__dbname)
            cursor = conn.cursor()
            result = cursor.execute(sql_query_sentences)
            cursor.close()
            conn.close()
            return result
        except:
            return []

    def createTables(self) -> None:
        result: list = []
        try:
            conn = sqlite3.connect(self.__dbname)
            cursor = conn.cursor()
            with open("manager/script.sql", "r") as script:
                cursor.executescript(script.read())
            conn.commit()
            result = cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            ).fetchall()
            cursor.close()
            conn.close()
            print(result)
        except Exception as e:
            print(f"Error:{e} al intentar crear las tablas.")

    def __getCellphoneNumber(self, contact_id: int) -> list:
        numbers: list = []
        try:
            rows = self.__getRows(
                f"FROM * FROM CellphoneNumber WHERE contact_id = {contact_id}"
            )
            for row in rows.fetchall():
                row_number = CellphoneNumber(row[0], row[1], row[2])
                numbers.append(row_number)
            return numbers
        except:
            return []

    def __getAddress(self, contact_id: int) -> list:
        addresses: list = []
        try:
            rows = self.__getRows(
                f"FROM * FROM Address WHERE contact_id ={contact_id} "
            )
            for row in rows.fetchall():
                row_address = Address(row[0], row[1], row[2])
                addresses.append(row_address)
            return addresses
        except:
            return []

    def getContacts(self) -> list:
        contacts: list = []
        try:
            rows = self.__getRows("SELECT * FROM Contact")
            for row in rows.fetchall():
                row_contact = Contact(row[0], row[1], row[2])
                row_contact.setAddress(self.__getAddress(row[0]))
                row_contact.setCellphoneNumbers(self.__getCellphoneNumber(row[0]))
                contacts.append(row_contact)
            return contacts
        except:
            return []

    def getContactNumber(self, contact_name: str) -> list:
        try:
            register = self.__getRows(
                f"SELECT * FROM Contact WHERE firtname like '%{contact_name}%'"
            )
            row = register.fetchone()
            result_contact = Contact(row[0], row[1], row[2])
            result_contact.setCellphoneNumbers(self.__getCellphoneNumber(row[0]))
            return list(result_contact)
        except:
            return []

    def getContactAddress(self, contact_name: str) -> list:
        try:
            register = self.__getRows(
                f"SELECT * FROM Contact WHERE firtname like '%{contact_name}%'"
            )
            row = register.fetchone()
            result_contact = Contact(row[0], row[1], row[2])
            result_contact.setAddress(self.__getAddress(row[0]))
            return list(result_contact)
        except:
            return []

    def addNewContact(self, contact: NewContact) -> None:
        try:
            conn = sqlite3.connect(self.__dbname)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Contact (firstname,lastname) VALUES (?,?)",
                contact.getInformation(),
            )
            conn.commit()
            cursor.close()
        except Exception as e:
            print(e)
