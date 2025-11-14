class A:
    def __init__(self,name,id):
      self.name=name
      self.__id=id

x=A("Radha",123)
print(x.name)
print(x._A__id)

        