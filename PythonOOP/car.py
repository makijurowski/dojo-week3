"""This is a Coding Dojo homework assignment."""


class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0.12

        if self.price > 10000:
            self.tax = 0.15

        self.display_all()

    def display_all(self):
        car_info = ('Price: ' + str(self.price) +
                    '\nSpeed: ' + self.speed +
                    '\nFuel: ' + self.fuel +
                    '\nMileage: ' + self.mileage +
                    '\nTax: ' + str(self.tax * 100) + '%')
        print(car_info + '\n')
        return self

car1 = Car(2000, '35mph', 'Full', '15mpg')
car2 = Car(1000, '5mph', 'Not Full', '15mpg')
car3 = Car(20000, '15mph', 'Full', '15mpg')
car4 = Car(2000, '60mph', 'Kind of Full', '15mpg')
car5 = Car(69000, '75mph', 'Half Full', '15mpg')
car6 = Car(20000000, '22mph', 'Empty', '15mpg')
