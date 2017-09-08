"""This is a Coding Dojo homework assignment."""


# Create a new class.
class md(object):
    # Initialize variables
    def __init__(self, num1):
        self.num1 = num1 or 0
        self.num_add = 0
        self.num_sub = 0
    # Method to add two numbers together.
    def add(self, num2):
        self.num2 = num2
        self.num_add = self.num1 + self.num2
        return self
    # Method to subtract one number from another.
    def subtract(self, num2):
        self.num2 = num2
        self.num_sub = self.num1 - self.num2
        return self
        
print md.add(2).add(2, 5).subtract(3, 2).result