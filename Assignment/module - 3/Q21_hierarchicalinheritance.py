# Q - 21  Write a Python program to show hierarchical inheritance.


class Numbers:
    def set_values(self, a, b):
        self.a = a
        self.b = b

class Addition(Numbers):
    def calculate(self):
        print("Addition:", self.a + self.b)

class Subtraction(Numbers):
    def calculate(self):
        print("Subtraction:", self.a - self.b)

class Multiplication(Numbers):
    def calculate(self):
        print("Multiplication:", self.a * self.b)


ob = Addition()
ob.set_values(10, 5)
ob.calculate()

ob = Subtraction()
ob.set_values(10, 5)
ob.calculate()

ob = Multiplication()
ob.set_values(10, 5)
ob.calculate()
