class House:
    def __init__(self):
        self.number_of_floors = 0

    def set_new_number_of_floors(self, floors):
        number_of_floors = floors
        print(number_of_floors)


hs = House()
hs.set_new_number_of_floors(5)
