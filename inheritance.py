class Person:
    def __init__(self, name, age,):
        self.name = name
        self.age = age
    
    def print_info(self):
        print(f'{self.name} is {self.age} years old')

class Teacher(Person):
    def __init__(self, name, age, subject):
        self.subject = subject
        
        Person.__init__(self, name, age)
    
    # def print_info(self):
    #     print(f'{self.name} is {self.age} years old and {self.subject} lesson')

myTeacher = Teacher('Dr. Hirani', 49, 'Computer Science')

myTeacher.print_info()
print(myTeacher.subject)     