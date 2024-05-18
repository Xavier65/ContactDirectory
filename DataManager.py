import sqlite3


class DataManager:
    def __init__(self, database: str) -> None:
        self.__connection = sqlite3.connect(database)
        self.__cursor = self.__connection.cursor()

    def __createTables(self):
        script:str = 
                """
                DROP TABLE IF EXISTS Contact;
                DROP TABLE IF EXISTS Address;
                DROP TABLE IF EXISTS CellphoneNumber;

                CREATE TABLE Contact(
                    id INTEGER NOT NULL,
                    firstname VARCHAR(32) NOT NULL,
                    lastname VARCHAR(32),
                    PRIMARY KEY(id autoincrement)
                );

                CREATE TABLE Address(
                    id INTEGER NOT NULL,
                    contact_id INTEGER NOT NULL,
                    address VARCHAR(32),
                    PRIMARY KEY(id autoincrement)
                );

                CREATE TABLE CellphoneNumber(
                    id INTEGER NOT NULL,
                        contact_id INTEGER NOT NULL,
                    cellphone_number VARCHAR(32) NOT NULL,
                    PRIMARY KEY(id autoincrement)
                );
            """
        try:
            cursor = self.__connection.cursor()
            cursor.executescript(
            self.__connection.commit()
            cursor.close()
        except Exception as e:
            cursor.close()
            print(f"Error: {e}")


    def validate(self):
        try:
            cursor = self.__connection.cursor()
            self.__createTables()
            result = cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table';"
            ).fetchall()
            cursor.close()
            return (len(result), result)
        except Exception as e:
            print(e)
            return False

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

