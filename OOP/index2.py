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
        self.tours.append(tour)
        print(f"Тур {self.id} добавлен в агенство")

    def show_available_tours(self):
        print("Доступные туры;")
        for tour in self.tours:
            if not tour._is_booked:
                tour.info()

    def book_tour(self, client, tour_id):
        for tour in self.tours:
            if tour.id == tour_id:
                if not tour._is_booked:
                    if client.pay(tour.price):
                        tour.book(client)
                        self._income += tour.price
                        print(f"Тур {tour_id} забронирован для клиента {client.name}")
                else:
                    print(f"Тур {tour_id} уже забронирован")
                return
        print(f"Тур с id {tour_id} не найден")

    def cancel_all_bookings(self):
        for tour in self.tours:
            if tour._is_booked:
                tour.cancel_booking()
        print("Все брони отменены")

    def show_status(self):
        print(f"Статус агентства {self.name}:")
        for tour in self.tours:
            tour.info()
        print(f"Текущая выручка: {self._income} сом")





agency = Agency("PKS travel")
t1 = Tour(1, 12000, 7)
t2 = Tour(2, 8000, 5)
t3 = Tour(3, 15000, 10)
agency.add_tour(t1)
agency.add_tour(t2)
agency.add_tour(t3)
c1 = Client("Ноила", 20000)
c2 = Client("шоди", 5000)
agency.show_available_tours()
agency.book_tour(c1, 1)
agency.book_tour(c2, 2)
agency.show_status()
agency.cancel_all_bookings()
agency.show_status()












        
        

    
 

