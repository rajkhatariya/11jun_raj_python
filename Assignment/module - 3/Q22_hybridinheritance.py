# Q - 22 Write a Python program to show hybrid inheritance.

class Numbers:
    def set_values(self, a, b):
        self.a = a
        self.b = b

class Addition(Numbers):
    def add(self):
        return self.a + self.b

class Multiplication(Numbers):
    def multiply(self):
        return self.a * self.b

class Result(Addition, Multiplication):
    def display(self):
        print("Addition:", self.add())
        print("Multiplication:", self.multiply())

obj = Result()
obj.set_values(10, 5)
obj.display()
