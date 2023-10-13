# # 1. Создать класс Computer (компьютер) с приватными атрибутами cpu и memory.
class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    # 2. Добавить в класс Computer приватный метод make_computations, в котором бы выполнялись арифметические вычисления(‘+’,  ‘-’,  ‘*’,  ‘/’ ) с атрибутами объекта cpu и memory результат вывести красиво с помощью ‘ f ’ .
    # 3. Добавить сеттеры и геттеры к существующим атрибутам и методу.
    @property
    def cpu(self):
        return self.__cpu

    # @cpu.setter
    # def cpu(self,new_cpu):
    #    self.cpu==new_cpu

    @property
    def memory(self):
        return self.__memory

    # @memory.setter
    # def memory(self,new_memory):
    #     self.memory==new_memory

    def __make_computations(self):
        print(f"Ядро вашего ноутбука - {self.cpu}, Оперативка - {self.memory} гб ")

    @property
    def make_computations(self):
        return self.__make_computations


characteristic1 = Computer(8, 16)
characteristic1.make_computations()


# 4. Создать класс Phone (телефон) с приватным полем sim_cards_list (список симкард)
# 5. Добавить сеттеры и геттеры к существующему атрибуту.
# 6. Добавить в класс Phone метод call с входящим параметром sim_card_number и call_to_number, в котором бы распечатывалась симуляция звонка в зависимости от переданного номера сим-карты (например: если при вызове метода передать число 1 и номер телефона, распечатывается текст “Идет звонок на номер +996 771 24 47 45” с сим-карты-1 - Beeline).
class Phone:
    def __init__(self, sim_cards_list, sim_cards_list2):
        self.__sim_cards_list = sim_cards_list
        self.__sim_cards_list2 = sim_cards_list2

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @property
    def sim_cards_list2(self):
        return self.__sim_cards_list2

    @sim_cards_list.setter
    def sim_cards_list(self, new_sim_cards_list):
        self.__sim_cards_list == new_sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list2(self, new_sim_cards_list2):
        self.__sim_cards_list2 == new_sim_cards_list2

    def __call__(self, sim_card_number, call_to_number):
        self.sim_cards_number = sim_card_number
        self.call_to_number = call_to_number
        print(
            f"Идет звонок на номер {self.sim_cards_number} , с сим-карты- {self.call_to_number}"
        )


mi = Phone("+996 771 24 47 45", "1-Beeline")

# 7. Создать класс SmartPhone и наследовать его от 2-х классов Computer и Phone.
# 8. Добавить метод в класс SmartPhone use_gps с входящим параметром location, который бы распечатывал симуляцию проложения маршрута до локации.
# 9. Добавить в класс SmartPhone метод add_memeory_card который бы увеличивал память телефона
# 10. Создать 1 объект компьютера, 1 объект телефона и 2 объекта смартфона
# 11. Распечатать информацию о созданных объектах с помощью метода info
# 12. Опробовать все возможные методы каждого объекта


class SmartPhone(Computer):
    def __init__(self, cpu, memory):
        super().__init__(cpu, memory)
    def add_memeory_card(self,cpu, memory):
        