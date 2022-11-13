class SistemaCadastral:
    
    def cadastrar(self, name: str, age: int) -> None:
        if self.__check_data():
            self.__storage_data(name=name, age=age)
        else:
            self.__show_error()


    def __check_data(self, name: str, age: int) -> bool:
        result = False
        if isinstance(name, str) and isinstance(age, int):
            result = True
        return result
    
    def __storage_data(self, name: str, age:int) -> None:
        print(f"data storaged {name} {age}")
    
    def __show_error(self) -> None:
        print("invalid data")