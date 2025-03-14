class VBase:
    __valid: bool

    def __init__(self) -> None:
        self.__valid = False
    
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
