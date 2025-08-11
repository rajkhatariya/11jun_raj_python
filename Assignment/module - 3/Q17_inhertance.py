# Q - 17   Write Python programs to demonstrate different types of inheritance (single, multiple, multilevel, etc.).

# single inheritance
class class1:
    def func(self):
        self.x=10
        self.y=20

class class2(class1):
    def sum(self):
        print("the sum is :",self.x+self.y)


# multiple inheritance
class perent1:

    def fact(self):
        self.a='Raj'
class perent2:

    def fact2(self):
        self.b=' Khatariya'

class child(perent1,perent2):

    def fact3(self):
        print("The name is :",self.a+self.b)


# multilevel inheritance
class multi1:

    def mul1(self):
        self.n1=int(input("enter the num :"))
        self.n2=int(input("enter the num2 :"))

class multi2(multi1):

    def mul2(self):
        self.mul=self.n1*self.n2

class multi3(multi2):

    def mul3(self):
        print("the multiplacation is :",self.mul)


ob1=class2()
ob2=child()
ob3=multi3()

ob1.func()
ob1.sum()
print('--------------------')
ob2.fact()
ob2.fact2()
ob2.fact3()
print('--------------------')
ob3.mul1()
ob3.mul2()
ob3.mul3()
             