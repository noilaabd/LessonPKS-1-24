class Tour:
    def __init__(self, id, price, days):
        self.__id = id
        self.__price = price
        self._is_booked = False
        self._client = None
        self._days = days 
    
    @property
    def id(self):
        return self.__id
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value>=5000:
            self.__price = value
        else:
            print("цена не может быть ниже 5000 сом")


    def book(self, client): #бронирует тур, делает его недоступным
        if self._is_booked:
            print("тур уже забронирован")
        else:
            self._is_booked = True
            self._client = client



    def cancel_booking(self): #отменяет бронь, делает тур доступным
        if not self._is_booked:
            print("тур не забронирован")
        else:
            self._is_booked = False
            self._client = None

    def info(self): 
        status = "забронирован" if self._is_booked else "свободен"
        client_name = self._client.name if self._client else "нет"
        print(f"тур id {self.__id}, цена {self.price} сом, дней: {self._days} статус: {status}, клиент: {client_name}")

        
class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def pay(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.name} оплатил {amount} сом")
            return True
        else:
            print(f"не достаточно средств у {self.name}")
            return False

    def add_balance(self, amount):
        self.balance += amount
        print(f"{self.name} пополнил баланс на {amount} сом")
        

    def info(self):
        print(f"Клиент {self.name}, баланс: {self.balance} сом")
        
        
       


class Agency:
    def __init__(self, name):
        self.name = name 
        self.tours = [] 
        self._income = 0  #доход агентства

    def add_tour(self, tour):
        self.tours.append()
        print(f"Тур {self.id} добавлен в агенство")

    def show_available_tours(self):
        pass

    
 
# Методы:
# add_tour(tour) — добавляет новый тур;
# show_available_tours() — показывает все свободные туры;
# book_tour(client, tour_id) — бронирует тур для клиента;
# cancel_all_bookings() — отменяет все активные брони;
# show_status() — показывает состояние всех туров и текущую выручку.
