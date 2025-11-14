class School:
    def __init__(self,school_name):
        self._school_name=school_name

class Teacher(School):
    def __init__(self, name,subject,school_name):
        super().__init__(school_name)
        self.name=name
        self.subject=subject
    
    def show_info(self):
        print(f"{self.name} teaches {self.subject} at {self._school_name}")

t1=Teacher("Mr. Smith","Math","Sunrise high school")
t1.show_info()