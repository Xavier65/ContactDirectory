import sqlite3


class DataManager:
    def __init__(self, database: str) -> None:
        self.__connection = sqlite3.connect(database)
        self.__cursor = self.__connection.cursor()

    def commit(self) -> None:
        self.__connection.commit()

    def getContacts(self) -> list:
        self.__contacts = self.__cursor.execute("SELECT * FROM Contact;")
        return self.__contacts.fetchall()

    def getCellphoneNumbers(self) -> list:
        self.__cellphone_numbers = self.__cursor.execute(
            "SELECT * FROM CellphoneNumber;"
        )
        return self.__cellphone_numbers.fetchall()

    def getAddresses(self) -> list:
        self.__addresses = self.__cursor.execute("SELECT * FROM Address;")
        return self.__addresses.fetchall()
