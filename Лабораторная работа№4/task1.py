class Cars:
    """Базовый класс автомобилей"""

    def __init__(self, brand: str, num_of_seats: int, colour: str, horsepower: int):
        self.brand = brand
        self.num_of_seats = num_of_seats
        self.colour = colour
        self.horsepower = horsepower

    def __str__(self):
        return f"Автомобиль марки {self.brand}. Количество посадочных мест {self.num_of_seats}. Цвет {self.colour}. Лошадиные силы {self.horsepower}"

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self.brand!r}, num_of_seats={self.num_of_seats!r}, colour:{self.colour!r}. horsepower:{self.horsepower!r})"

    def change_colour(self, colour):
        """Метод, который изменяет цвет автомобиля"""

    def horsepower_upgrade(self, horsepower):
        """Метод, каоторый увеличичает количество лошадиных сил"""



class PassengerCar(Cars):
    """Дочерний класс легковых автомобилей"""

    def __init__(self, brand: str, num_of_seats: int, colour: str, horsepower: int, trunk_vol: float): # trunk_vol- объем багажника
        super().__init__(brand, num_of_seats, colour, horsepower)
        self.trunk_vol = trunk_vol

    def __str__(self):
        return f"Автомобиль марки {self.brand}. Количество посадочных мест {self.num_of_seats}. Цвет {self.colour}. Лошадиные силы {self.horsepower}. Объем багажника {self.trunk_vol}"

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self.brand!r}, num_of_seats={self.num_of_seats!r}, colour:{self.colour!r}, horsepower:{self.horsepower!r}, trunk_vol{self.trunk_vol})"



class Truck(Cars):
    """Дочерний класс грузовых автомобилей"""

    def __init__(self, brand: str, num_of_seats: int, colour: str, horsepower: int):
        super().__init__(brand, num_of_seats, colour, horsepower)

    def horsepower_upgrade(self, horsepower):
        """Метод, каоторый увеличичает количество лошадиных
        пергруден для грузовых автомобилей и не будет давать возможность
        этому классу увеличивать количество лошидиных сил, так как чеще всего
        такакя возможность ограничена законом. То есть метод не даст изменить количество
        лошадиных сил у грузового автомобиля"""


if __name__ == "__main__":

    car_1 = PassengerCar("BMW", 5, "RED", 210, 520.3)
    print(car_1)
    car_2 = Truck("Камаз", 3, "Black", 180)
    print(car_2)
    pass
