class NewContact:
    def __init__(self, contact: dict) -> None:
        self.__firstname: str = contact["firstname"]
        self.__lastname: str = contact["lastname"]

    def getInformation(self) -> tuple:
        return (self.__firstname, self.__lastname)


class Contact:
    def __init__(self, contact: dict) -> None:
        self.__id: int = contact["id"]
        self.__firstname: str = contact["firstname"]
        self.__lastname: str = contact["lastname"]
        self.__cellphone_numbers: list = []
        self.__address: list = []

    def getId(self) -> int:
        return self.__id

    def getFirstname(self) -> str:
        return self.__firstname

    def getLastname(self) -> str:
        return self.__lastname

    def getCellphoneNumbers(self) -> list:
        return self.__cellphone_numbers

    def getAddress(self) -> list:
        return self.__address

    def setFirstname(self, first_name: str) -> None:
        self.__firstname = first_name

    def setLastname(self, lastname: str) -> None:
        self.__lastname = lastname

    def setCellphoneNumbers(self, cellphone_numbers: list) -> None:
        self.__cellphone_numbers = cellphone_numbers

    def setAddress(self, address: list) -> None:
        self.__address = address

    def show(self):
        return (
            self.__id,
            self.__firstname,
            self.__lastname,
            self.__cellphone_numbers,
            self.__address,
        )
