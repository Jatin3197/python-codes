class User:
    def __init__(self,username,password):
        self.username=username
        self.__password=password

    

    def login(self,username,password):
        if self.username==username and self.__password==password:
            print(f"Login successfully")
        else:
            print("invalid username and password.")

u1=User("Alice","abc123")
u1.login("Alice","abc123")
u1.login("Alice","3145a")