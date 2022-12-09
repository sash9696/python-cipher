#inheritance

class Person: #parent class
 def __init__(self,name, age):
  self.name = name
  self.age = age
  
 def printDetails(self):
  print(self.name, self.age)
  
  
person1 = Person("John", 30)


class Student(Person):
 def __init__(self,name,age,year):
  #Person.__init__(self, name, age)
  super().__init__(name,age)
  self.admissionYear = year
  
 def greetings(self):
  print("Welcome", "to the class of" , self.admissionYear, self.name)
 
 #def printDetails(self):
  #print(self.name, self.age,self.admissionYear)
 
student1 = Student("peter", 15, 2022)
student1.printDetails()
