# Q - 19 Write a Python program to show multilevel inheritance.
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

ob=multi3()
ob.mul1()
ob.mul2()
ob.mul3()
