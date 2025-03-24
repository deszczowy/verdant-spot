from outline import VProject, VCommand

class VSaver:

    def __init__(self) -> None:
        self.data = []
    
    def store(self, project_data: VProject, file_name: str) -> None:
        self.__start()
        self.__finish()
        self.__store()
    
    def __start(self) -> None:
        self.data.append(VCommand.VerdantSpotStart)
    
    def __finish(self) -> None:
        self.data.append(VCommand.Stop)
    
    def __store(self) -> None:
        print(self.data)