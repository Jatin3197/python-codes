class Patient:
    def __init__(self,name,age,disease,patient_id):
        self.name=name
        self.age=age
        self._disease=disease
        self.__patient_id=patient_id

    def get_patient_id(self):
        return self.__patient_id
    
    def set_patient_id(self,new_id):
        print("Patient id can not be changed!")

    def show_details(self):
        print(f"Name:{self.name} ,Age:{self.age} ,Disease:{self._disease}")\
        
p1=Patient("Alice",25,"Flu","P12345")
p1.show_details()
print("Patient id",p1.get_patient_id())
p1.set_patient_id(1)
        