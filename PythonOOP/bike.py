class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def display_info(self):
        print('This bike costs $' + str(self.price) + ' dollars ' +
              'with a max speed of ' + self.max_speed + '. It has been ' +
              'ridden for a total of ' + str(self.miles) + ' miles.')
        return self

    def ride(self):
        print 'Riding...'
        self.miles += 10
        return self

    def reverse(self):
        print 'Reversing...'
        self.miles -= 5
        return self

    def repeat(self, n, my_function):
        self.n = n
        for i in range(self.n):
            my_function()
        return self


bike1 = Bike(200, '25mph', 5)
bike2 = Bike(150, '15mph', 2)
bike3 = Bike(500, '50mph', 0)

bike1.repeat(3, bike1.ride).repeat(1, bike1.reverse).repeat(1, bike1.display_info)
