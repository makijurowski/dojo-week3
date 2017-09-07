"""This is a Coding Dojo homework assignment."""


class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1

    def run(self):
        self.health -= 5

    def display_health(self):
        print self.health

    def repeat(self, n, my_function, *args):
        self.n = n
        for i in range(self.n):
            my_function(*args)
        return self


class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        self.health = 150

    def pet(self):
        self.health += 5


class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)
        self.health = 170

    def fly(self):
        self.health -= 10

    def display_health(self):
        super(Dragon, self).display_health()
        print 'I am a dragon!'

# Provided test cases.
animal1 = Animal('ChiDog', 100)
animal1.repeat(3, animal1.walk).repeat(
    2, animal1.run).repeat(1, animal1.display_health)
animal2 = Animal('Goose', 25)
animal2.repeat(3, animal2.walk).repeat(
    2, animal2.run).repeat(1, animal2.display_health)
animal3 = Dragon('Green', 300)
animal3.repeat(3, animal3.walk).repeat(
    2, animal3.run).repeat(1, animal3.display_health)
animal4 = Dog('Bassett', 200)
animal4.repeat(3, animal4.walk).repeat(
    2, animal4.run).repeat(1, animal4.display_health)
