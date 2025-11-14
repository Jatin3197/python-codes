class Car:
    def __init__(self,brand,speed):
        self.brand=brand
        self.__speed=speed

    def get_speed(self):
        return self.__speed
    
    def set_speed(self,new_speed):
        if new_speed>0:
            self.__speed=new_speed
        else:
            print("Speed cannot be negative!")

c1=Car("Toyata",120)
print(c1.brand)

print(c1.get_speed())
c1.set_speed(150)
print(c1.get_speed())

        