class parent1:
    def show(self):
        print("It is from parent1")

class parent2(parent1):
    def show(self):
        print(" it is from parent2")


class parent3(parent1):
    def show(self):
        print(" it is from parent3")

a1=parent1()
a2=parent2()
a3=parent3()

a1.show()
a2.show()
a3.show()

    