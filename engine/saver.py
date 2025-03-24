from outline import VProject, VCommand

class VSaver:

    def __init__(self) -> None:
        self.data = []
    
    def store(self, project_data: VProject, file_name: str) -> None:
        self.__start()
        self.__store_project_info(project_data)
        self.__finish()
        self.__store()
    
    def __start(self) -> None:
        self.data.append(VCommand.VerdantSpotStart)
    
    def __store_project_info(self, project_data: VProject) -> None:
        self.__append_data(project_data.Info.Name, VCommand.Name)
        self.__append_data(project_data.Info.Description, VCommand.Desctiption)
        self.__append_data(project_data.Info.Author, VCommand.Author)
        self.__append_data(project_data.Info.Size.to_store(), VCommand.MapSize)
        self.__append_data(project_data.Info.Center.to_store(), VCommand.Center)
    
    def __finish(self) -> None:
        self.data.append(VCommand.Stop)
    
    def __append_data(self, data: str, command: str) -> None:
        self.data.append(data)
        self.data.append(command)
    
    def __store(self) -> None:
        print(self.data)