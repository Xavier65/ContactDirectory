import sqlite3

from schemas.Contact import Contact, NewContact
from schemas.CellphoneNumber import CellphoneNumber, NewCellphoneNumber
from schemas.Address import Address, NewAddress


class DataManager:
    def __init__(self, database: str) -> None:
        self.__dbname: str = database

    def __getRows(self, sql_query_sentences: str) -> sqlite3.Cursor | list:
        try:
            conn = sqlite3.connect(self.__dbname)
            cursor = conn.cursor()
            return cursor.execute(sql_query_sentences)
        except Exception as e:
            print(f"Error:{e} -> getRows")

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
        except Exception as e:
            print(f"Error:{e} al intentar crear las tablas.")

    def __getContact(self, contact_id: int):
        try:
            conn = sqlite3.connect(self.__dbname)
            cursor = conn.cursor()
            result = cursor.execute(f"SELECT * FROM Contact WHERE id = {contact_id}")
            return result.fetchone()
        except Exception as e:
            print(e)

    def __getCellphoneNumber(self, contact_id: int) -> list:
        numbers: list = []
        try:
            rows = self.__getRows(
                f"SELECT * FROM CellphoneNumber WHERE contact_id = {contact_id}"
            )
            for row in rows.fetchall():
                row_number = CellphoneNumber(row[0], row[1], row[2])
                numbers.append(row_number.getCellphoneNumber())
            return numbers
        except:
            return []

    def __getAddress(self, contact_id: int) -> list:
        addresses: list = []
        try:
            rows = self.__getRows(
                f"SELECT * FROM Address WHERE contact_id ={contact_id} "
            )
            for row in rows.fetchall():
                row_address = Address(row[0], row[1], row[2])
                addresses.append(row_address.getAddress())
            return addresses
        except Exception as e:
            print(e)
            return []

    def getAllContacts(self) -> list:
        contacts: list = []
        try:
            rows = self.__getRows("SELECT * FROM Contact")
            for row in rows.fetchall():
                row_contact = Contact(row[0], row[1], row[2])
                row_contact.setAddress(self.__getAddress(row[0]))
                row_contact.setCellphoneNumbers(self.__getCellphoneNumber(row[0]))
                contacts.append(row_contact.show())
            return contacts
        except:
            return []

    def getContactNumber(self, cellphoneNumber: str):
        try:
            register = self.__getRows(
                f"SELECT * FROM CellphoneNumber WHERE cellphone_number like '%{cellphoneNumber}%'"
            )
            row = register.fetchone()
            result = self.__getContact(row[1])
            contact = Contact(result[0], result[1], result[2])
            contact.setCellphoneNumbers(self.__getCellphoneNumber(row[1]))
            contact.setAddress(self.__getAddress(row[1]))
            return contact.show()
        except Exception as e:
            print(f"Error:{e} -> getContactNumber")

    def getContactAddress(self, address: str) -> list:
        try:
            register = self.__getRows(
                f"SELECT * FROM Address WHERE address like '%{address}%'"
            )
            row = register.fetchone()
            result = self.__getContact(row[1])
            contact = Contact(result[0], result[1], result[2])
            contact.setCellphoneNumbers(self.__getCellphoneNumber(row[1]))
            contact.setAddress(self.__getAddress(row[1]))
            return contact.show()
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

    def addNewAddress(self, address: NewAddress) -> None:
        try:
            conn = sqlite3.connect(self.__dbname)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Address (contact_id, address) VALUES (?,?)",
                address.getInformation(),
            )
            conn.commit()
            cursor.close()
        except Exception as e:
            print(e)

    def addNewCellphoneNumber(self, cellphoneNumber: NewCellphoneNumber) -> None:
        try:
            conn = sqlite3.connect(self.__dbname)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO CellphoneNumber (contact_id, cellphone_number) VALUES (?,?)",
                cellphoneNumber.getInformation(),
            )
            conn.commit()
            cursor.close()
        except Exception as e:
            print(e)
