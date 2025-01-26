class Dog:
    # this is a blank class
    pass

pepper = Dog()
print(pepper)

class ClassSchedule:
   def __init__(self, course): #__init__() function is used as the constructor and is called when creating an object.
       self.course = course
  
   def __del__(self): # Python’s built-in __del__() method represents the destructor in a class
       print('You successfully deleted your schedule')
 
       
# first = ClassSchedule('Medicine')
# print(first.course)

sched = ClassSchedule('Chemistry')
del sched