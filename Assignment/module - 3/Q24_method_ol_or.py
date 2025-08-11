# Q - 24 Write Python programs to demonstrate method overloading and method overriding. 


class Parent:
    def add(self, a=0, b=0):
        print("Sum:", a + b)

    def show(self):
        print("Parent class method")

class Child(Parent):
    def show(self):
        print("Child class method")

obj = Child()

obj.add(10, 20)   
obj.add(5)       

obj.show()
