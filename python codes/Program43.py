class Parent1:
    def show(self):
        print("This is from Parent1")

class Parent2(Parent1):
    def show1(self):
        print("This is from Parent2")

class Parent3(Parent2):
    def show2(self):
        print("This is a Parent3")


class Parent4():
    def show3(self):
        print("This is a Parent4")

class Parent5(Parent1,Parent4):
    def show4(self):
        print("This is a Parent5")


ob=Parent5()
ob.show()
ob.show3()
ob.show4()
ob1=Parent3()
ob1.show()
ob1.show1()
ob1.show2()

