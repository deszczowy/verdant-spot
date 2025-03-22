class VBase:

    def __init__(self) -> None:
        self.__valid = False
        self.__id = None
    
    def set_id(self, id: int) -> None:
        self.__id = id

    def id(self) -> int:
        if self.__id is None:
            from random import randrange
            return int(randrange(2**63, 2**64))
        else:
            return self.__id
    
    def is_valid(self) -> bool:
        return self.__valid

    def _set_valid(self) -> None:
        self.__valid = True

    def _is_true(self, string) -> bool:
        return string == "T"
    
    def to_debug(self) -> str:
        pass
    
    def to_store(self) -> str:
        pass
