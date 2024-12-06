class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        i = 0
        print(self.name, self.number_of_floors)
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f"Такого этажа не существует")
        else:
            for i in range(new_floor):
                print(i + 1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, Количество этажей: {self.number_of_floors} ')

    def __eq__(self, other):  # ==
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):# (<)
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other): # (<=)
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other): # (>)
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other): # (>=)
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other): # (!=)
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return self

    def __radd__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return self

    def __iadd__(self, value):
        self.number_of_floors += value
        return self

open_spaces = House("ЖК Просторы", 20)
parking = House("Парковка", 4)
print(open_spaces)
print(parking)
print(open_spaces == parking)
print(open_spaces < parking)
print(open_spaces <= parking)
print(open_spaces > parking)
print(open_spaces >= parking)
print(open_spaces != parking)
print(parking + 16)
print(open_spaces == parking)
print(open_spaces + 10)
print(parking.__iadd__(10))

# print(str(open_spaces))
# print(len(open_spaces))
# print(str(parking))
# print(len(parking))
# open_spaces.go_to(5)
# parking.go_to(-5)
# parking.go_to(0)