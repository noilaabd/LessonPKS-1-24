# ########### Задача Симуляция компьютерного клуба

# создаём систему для комп клуба, где можно бронировать и оплачивать места.
# Каждый компьютер имеет свою цену за час, статус (свободен/занят), и время, когда его забронировали.
# Клиенты могут садиться за компьютер, играть и оплачивать время.
# Владелец клуба может смотреть выручку и управлять компьютерами.

class Computer:
    def __init__(self, id, hourly_rate, is_busy, current_client, start_time):
        self.__id = id
        self.__hourly_rate = hourly_rate
        self._is_busy = False
        self._current_client = None
        self._start_time = 0
        
    @property
    def id(self):
        return self.__id

    @property
    def hourly_rate(self):
        return self.__hourly_rate
    
    @hourly_rate.setter
    def hourly_rate(self, new_rate):
        if new_rate >= 50 and new_rate<=1000:
            self.__hourly_rate = new_rate

    def start_session(self, client, hours):
        if self._is_busy:
            print("Комп занят")
            return False
        cost = self.__hourly_rate * hours
        if client.pay(cost):
            self._is_busy = True
            self._current_client = client
            self._start_time = hours
            print(f"{client} занял комп {self.id} на {hours}час, за {cost}сом")
        else:
            print(f"Клиента {client.name} не хватает денег")
        
    def end_session(self):
        if not self._is_busy:
            print("Компьютер не использовался")
            return 0 
        self._is_busy = False
        income = self.__hourly_rate*self._start_time
        client_name = self._current_client.name
        print("Сессия завершена")
        self._current_client = None
        self._start_time = 0
        return income
    
    def info(self):
        status = 'Занят' if self._is_busy else "Свободен"
        return f"комп {self.id} {status} {self.__hourly_rate} сом/ч"
    
class Client:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance

    @property
    def balance(self):
        return self._balance
    

    def add_balance(self, amount):
        if amount >0 and amount<=10000:
            self._balance += amount
            print(f"Баланс пополнен на {amount}сом, теперь у вас {self._balance}")
        else:
            print("Введите корректное значение на пополнение")
            return False

    def pay(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return True
        return False


    def info(self):
        print(f"Имя: {self.name} на карте: {self._balance} сом")


class Club:
    def __init__(self, name):
        self.name = name
        self.computers = []
        self._income = 0


    def add_computer(self, computer):
        self.computers.append(computer)
        print(f"Комп добавлен {computer.id} с тарифом {computer.hourly_rate} сом/ч")

    def find_free_computer(self):
        for comp in self.computers:
            if comp._is_busy == False:
                return comp
        return None
    

    def serve_client(self, client, hours):
        free_comp = self.find_free_computer()
        if not free_comp:
            print("Нет свободных компов")
            return
        if free_comp.start_session(client, hours):
            self._income += free_comp.hourly_rate * hours


    def end_all_sessions(self):
        for comp in self.computers:
            self._income += self.end_session()
            print("Все закрыто")

    def show_status(self):
        print(f"Клуб {self.name}")
        for comp in self.computers:
            print(comp.info())
        print(f"Выручка клуба {self._income} сом")


    @property
    def income(self):
        return self._income
    

b = Club("HuneHunerClub")
b.add_computer(Computer(1,100))
b.add_computer(Computer(2,150))
b.add_computer(Computer(3,180))
x = Client('Malika', 500)
y = Client('Aliya', 100)
b.serve_client(y, 2)
b.serve_client(x, 3.5)
b.show_status()
        




            

        

# 1. класс Computer
# Инкапсулированный класс, представляющий компьютер.
# Атрибуты:
# __id — уникальный номер (инкапсулированный, доступ через свойство).
# __hourly_rate — цена за час (инкапсулированный, управляется через @property).
# _is_busy — защищённый атрибут (True/False).
# _current_client — текущий клиент или None.
# _start_time — время начала сессии.
# Методы:
# start_session(client, hours) — запускает сессию, делает компьютер занятым.
# end_session() — завершает сессию, считает оплату.
# info() — краткое состояние компьютера.
# Свойства:
# hourly_rate — с @property и @setter: цена не может быть ниже 50 сом.
# id — только для чтения (@property, без setter).

# 2. Client
# Атрибуты: name, balance
# Методы:
# pay(amount) — уменьшает баланс, если хватает денег.
# add_balance(amount) — пополнение счёта.
# info() — информация о клиенте.

# 3. Club
# Атрибуты: name, computers — список объектов Computer
# _income — защищённый атрибут, выручка клуба.
# Методы:
# add_computer(computer)
# find_free_computer()
# serve_client(client, hours) — находит свободный комп, запускает сессию.
# end_all_sessions() — завершает все активные сессии и увеличивает доход клуба.
# show_status() — показывает состояние всех компьютеров и доход.