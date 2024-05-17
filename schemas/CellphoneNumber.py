class CellphoneNumber:
    def __init__(self, id: int, contact_id: int, cellphone_number: str) -> None:
        self.__id: int = id
        self.__contact_id: int = contact_id
        self.__cellphone_number: str = cellphone_number

    def getId(self) -> int:
        return self.__id

    def getContactId(self) -> int:
        return self.__contact_id

    def getCellphoneNumber(self) -> str:
        return self.__cellphone_number

    def setContactId(self, contact_id: int) -> None:
        self.__contact_id = contact_id

    def setCellphoneNumber(self, cellphone_number: str) -> None:
        self.__cellphone_number = cellphone_number
