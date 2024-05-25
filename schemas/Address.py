class NewAddress:
    def __init__(self, address: dict) -> None:
        self.__contact_id: int = address["contact_id"]
        self.__address: str = address["address"]

    def getInformation(self) -> tuple:
        return (self.__contact_id, self.__address)


class Address:
    def __init__(self, address: dict) -> None:
        self.__id: int = address["id"]
        self.__contact_id: int = address["contact_id"]
        self.__address: str = address["address"]

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
