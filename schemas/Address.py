class Address:
    def __init__(self, id: int, contact_id: int, address: str) -> None:
        self.__id: int = id
        self.__contact_id: int = contact_id
        self.__address: str = address

    def getId(self) -> int:
        return self.__id

    def getContactId(self) -> int:
        return self.__contact_id

    def getAddress(self) -> str:
        return self.__address

    def setContactId(self, contact_id: int) -> None:
        self.__contact_id = contact_id

    def setAddress(self, address: str) -> None:
        self.__address = address
