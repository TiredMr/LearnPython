class ClassSchedule1:
   def __init__(self, course, instructor):
       self.course = course # public
       self.instructor = instructor # public
  
   def display_course(self):
       print(f'Course: {self.course}, Instructor: {self.instructor}')
       
sched1 = ClassSchedule1('Chemistry', 'Mr. Doe') # initializing
 
sched1.display_course() # prints Course: Chemistry, Instructor: Mr. Doe
print(sched1.course) # prints 'Chemistry'

#==================================================================================

class ClassSchedule2:
   def __init__(self, course, instructor):
       self._course = course # protected
       self._instructor = instructor # protected
  
   def display_course(self):
       print(f'Course: {self._course}, Instructor: {self._instructor}')
 
sched2 = ClassSchedule2('Biology', 'Ms. Smith')
sched2.display_course()

#====================================================================================

class ClassSchedule3:
   def __init__(self, course, instructor):
       self.__course = course # private
       self.__instructor = instructor # private
  
   def display_course(self):
       # public
 
       print(f'Course: {self.__course}, Instructor: {self.__instructor}')
 
sched3 = ClassSchedule3('Biology', 'Ms. Smith')
 
# sched3.__course # this will throw an Attribute Error because we're trying to access a private member
 
sched3.display_course() # this won't throw an Attribute Error because this method is public
