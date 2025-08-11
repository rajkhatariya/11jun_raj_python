# Q - 20  Write a Python program to show multiple inheritance.

class perent1:

    def fact(self):
        self.a='Raj'
class perent2:

    def fact2(self):
        self.b=' Khatariya'

class child(perent1,perent2):

    def fact3(self):
        print("The name is :",self.a+self.b)

ob=child()
ob.fact()
ob.fact2()
ob.fact3()
