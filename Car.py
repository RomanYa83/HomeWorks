class Car:
    price = 100000

    def horse_power(self):
        print('Мощность - 80 л.с.')

class Nissan(Car):
    price = 80000
    def horse_power(self):
        print('Мощность - 120 л.с.')


class Kia(Car):
    price = 110000
    def horse_power(self):
        print('Мощность - 200 л.с.')


car = Car()
print('Стоимость авто', car.price)
car.horse_power()
print('=' * 25)
car_1 = Nissan()
print('Стоимость авто', car_1.price)
car_1.horse_power()
print('=' * 25)
car_2 = Kia()
print('Стоимость авто', car_2.price)
car_2.horse_power()
