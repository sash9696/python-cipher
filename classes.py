#Functional programming and OOPS (Object Oriented Programming)

#python is an oops language
#Object is nothing but a collection of data
#Classes are used to create one or more objects


#create an object 

class MyClass:
	a = 40

object1 = MyClass()
print(object1.a)




class Person:
	
    def __init__(self, name, age):
    	
        self.name = name
        self.age = age
        
person1 = Person("John", 40)
person2 = Person("Peter", 20)

print(person1.name)
print(person2.name)



#object methods

class Person:
	
    def __init__(abc, name, age):
    	
        abc.name = name
        abc.age = age
        
    def myFunc(abc):
    	print("My name is  " + abc.name)
        
person1 = Person("John", 40)
person2 = Person("Peter", 20)

person1.myFunc()
person2.myFunc()




myList = [10, 20, 30]

myList.append(40)

print(myList)


#the reference to the current instance of the class will always be the first parameter of the function that u define inside the class