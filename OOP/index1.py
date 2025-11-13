# ########### Задача Симуляция компьютерного клуба

# создаём систему для комп клуба, где можно бронировать и оплачивать места.
# Каждый компьютер имеет свою цену за час, статус (свободен/занят), и время, когда его забронировали.
# Клиенты могут садиться за компьютер, играть и оплачивать время.
# Владелец клуба может смотреть выручку и управлять компьютерами.

class Computer:
    def __init__(self, id, hourly_rate, is_busy, current_client, start_time):
        self.__id = id
        self.__hourly_rate = hourly_rate
        self._is_busy = is_busy
        self._current_client = current_client
        self._start_time = start_time

    @property
    def hourly_rate(self):
        return self.__hourly_rate
                
    @hourly_rate.setter
    def hourly_rate(self, rate):
        if rate < 100:
            print("минимум за час 100 сом")
        self.__hourly_rate = rate

    @property
    def id(self):
        return self.__id
    
    def start_session(self, client, hours):
        if self._is_busy:
            print("Компьютер занят")
        self._is_busy = True
        self._current_client = client
        self._start_time = hours  # упрощение для примера

    def end_session(self):
        if not self._is_busy:
            print("Компьютер не занят")
        




            

        

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