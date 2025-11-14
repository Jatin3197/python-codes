class ATM:
    def __init__(self,card_number,pin,balance):
       self.card_number=card_number
       self.__pin=pin
       self.__balance=balance
    def check_pin(self,pin):
        return self.__pin==pin
    
    def Withdraw(self,pin,amount):
        if self.check_pin(pin):
            if amount <=self.__balance:
                self.__balance-=amount
                print(f"Withdrawn ${amount}. Remaining balance:${self.__balance}")
            else:
                print("Insufficient balance!")
        else:
                print("Invalid Pin!")

    def deposit(self,pin,amount):
         if self.check_pin(pin):
                self.__balance+=amount
                print(f"Deposited ${amount}. New balance:${self.__balance}")
         else:
                print("Invalid Pin")
        
atm1=ATM("1234-5678",4321,1000)
atm1.Withdraw(4321,300)
atm1.deposit(4321,500)
atm1.deposit(2211,2882)