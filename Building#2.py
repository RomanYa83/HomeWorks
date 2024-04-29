from random import randint


class Building:
    total = 0

    def __init__(self):
        Building.total += 1


district = []
district_size = randint(0, 40)
while len(district) < district_size:
    b = Building()
    district.append(b)
print(Building.total)
