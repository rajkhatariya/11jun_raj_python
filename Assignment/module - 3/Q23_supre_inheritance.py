# Q - 23 ) Write a Python program to demonstrate the use of super() in inheritance. 

class Addition:
    def calculate(self, a, b):
        self.a = a
        self.b = b
        print("Sum from Addition class:", self.a + self.b)

class Addition2(Addition):
    def calculate(self, a, b, c):
        super().calculate(a, b)
        print("Final sum from AdvancedAddition class:", a + b + c)

obj = Addition2()
obj.calculate(10,20,30)
