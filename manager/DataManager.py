import sqlite3

from schemas.Contact import Contact, NewContact
from schemas.CellphoneNumber import CellphoneNumber, NewCellphoneNumber
from schemas.Address import Address, NewAddress


class DataManager:
    def __init__(self, database: str) -> None:
        self.__dbname: str = database

    def __getRows(self, sql_query_sentences: str) -> sqlite3.Cursor:
        try:
            conn = sqlite3.connect(self.__dbname)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(sql_query_sentences)
            return cursor
        except Exception as e:
            print(f"Error:{e} -> getRows")

    def createTables(self) -> None:
        try:
            conn = sqlite3.connect(self.__dbname)
            cursor = conn.cursor()
            with open("manager/script.sql", "r") as script:
                cursor.executescript(script.read())
            conn.commit()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            cursor.close()
            conn.close()
            print("Tablas creadas")
        except Exception as e:
            print(f"Error:{e} al intentar crear las tablas.")

    def __getContact(self, contact_id: int) -> dict:
        try:
            contact = self.__getRows(f"SELECT * FROM Contact WHERE id = {contact_id}")
            return dict(contact.fetchone())
        except Exception as e:
            print(e)

    def __getCellphoneNumber(self, contact_id: int) -> list:
        numbers: list = []
        try:
            rows = self.__getRows(
                f"SELECT * FROM CellphoneNumber WHERE contact_id = {contact_id}"
            )
            for row in rows.fetchall():
                row_number = CellphoneNumber(dict(row))
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
                row_address = Address(dict(row))
                addresses.append(row_address.getAddress())
            return addresses
        except Exception as e:
            print(e)
            return []

    def getAllContacts(self) -> list:
        try:
            rows = self.__getRows("SELECT * FROM Contact")
            return [dict(row) for row in rows.fetchall()]
        except:
            return []

    def getContactNumber(self, cellphoneNumber: str):
        try:
            register = self.__getRows(
                f"SELECT * FROM CellphoneNumber WHERE cellphone_number like '%{cellphoneNumber}%'"
            )
            row = dict(register.fetchone())
            contact = self.__getContact(row["contact_id"])
            row_contact = Contact(contact)
            row_contact.setCellphoneNumbers(
                self.__getCellphoneNumber(row["contact_id"])
            )
            row_contact.setAddress(self.__getAddress(row["contact_id"]))
            return row_contact.show()
        except Exception as e:
            print(f"Error:{e} -> getContactNumber")

    def getContactAddress(self, address: str) -> list:
        try:
            register = self.__getRows(
                f"SELECT * FROM Address WHERE address like '%{address}%'"
            )
            row = dict(register.fetchone())
            contact = self.__getContact(row["contact_id"])
            row_contact = Contact(contact)
            row_contact.setCellphoneNumbers(
                self.__getCellphoneNumber(row["contact_id"])
            )
            row_contact.setAddress(self.__getAddress(row["contact_id"]))
            return row_contact.show()
        except:
            return []

    def addNewContact(
        self, contact: NewContact, address: NewAddress, number: NewCellphoneNumber
    ) -> None:
        try:
            conn = sqlite3.connect(self.__dbname)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Contact (firstname,lastname) VALUES (?,?)",
                contact.getInformation(),
            )
            cursor.execute(
                "INSERT INTO Address (contact_id, address) VALUES (?,?)",
                address.getInformation(),
            )
            cursor.execute(
                "INSERT INTO CellphoneNumber (contact_id, cellphone_number) VALUES (?,?)",
                number.getInformation(),
            )
            conn.commit()
            cursor.close()
        except Exception as e:
            print(e)
