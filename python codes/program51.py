class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"Deposited {amount},new balance:{self.__balance}")

        else:
            print("Insufficient Balance")

    def withdraw(self,amount):
        if 0 < amount <=self.__balance:
            self.__balance-=amount
            print(f"Withdraw {amount} ,New Balance:{self.__balance}")
        
        else:
            print("Invalid withdrawl amount")

    def get_balance(self):
        return self.__balance
    
account=BankAccount("Jatin",1000)
account.deposit(500)
account.withdraw(200)
print("Final Balance:",account.get_balance())