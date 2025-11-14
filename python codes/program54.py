class Car:
    def __init__(self,brand,model,price):
        self.brand=brand
        self._model=model
        self.__price=price
    def show_details(self):
        print(f"Brand:{self.brand}")
        print(f"Model:{self._model}")
        print(f"Price:{self.__price}")
    
    def get_price(self):
        return self.__price
    
    def set_price(self,new_price):
        if new_price>0:
            self.__price=new_price
        else:
            print("Invalid Price")

Car1=Car("Toyata","Corolla",2000000)
print("Public:",Car1.brand)

print("Protected:",Car1._model)

print("Private:",Car1.get_price())

Car1.set_price(2500000)


print("Private:",Car1.get_price())

Car1.show_details()



        