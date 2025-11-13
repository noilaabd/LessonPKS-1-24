#### @property
# getter
# setter
# deleter
class Teacher:
    def __init__(self, name, phone):
        self.name = name 
        self._phone = phone 
    
    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(sefl, value):
        print("сеттер сработал")
       

    @phone.deleter
    def phone(self):
        print("удалили номер deleter")
        del self.__phone

    def info(self):
        return f"{self.name} {self.__phone}"
    
t = Teacher('Ali', 770770770)
t.phone = 45
print(t.phone)
# del t.phone
print(t.info())
        