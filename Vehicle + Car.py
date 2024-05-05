class Vehicle:
    vehicle_type = 'none'


class Car:
    price = '$' + str('1`000`000')


    def horse_powers(self, hp):
        return f"Количество лошадиных сил: {hp}"

class Nissan(Car, Vehicle):
    price = '$' + str('500`000')
    vehicle_type = 'SportCar'

    def horse_powers(self, hp):
        return f"Количество лошадиных сил: {hp}"


nis = Nissan()
print(nis.horse_powers(1000))
print(nis.price, nis.vehicle_type)
