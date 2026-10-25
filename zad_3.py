class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (f"Dom: {self.address}, {self.area} m2, "
                f"pokoje: {self.rooms}, działka: {self.plot} m2, "
                f"cena: {self.price} zł")


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (f"Mieszkanie: {self.address}, {self.area} m2, "
                f"pokoje: {self.rooms}, piętro: {self.floor}, "
                f"cena: {self.price} zł")


if __name__ == "__main__":
    house = House(150, 5, 950000, "Kraków, Lipowa 7", 600)
    flat = Flat(52, 2, 610000, "Kraków, Karmelicka 15/4", 3)

    print(house)
    print(flat)
