


# def printName(name, age):
#     print('My name is ' + name + "and my age is " + age)

# printName('john','10',)
# printName('peter', '20',)
# printName('abc','30', )
# printName('efg', '40',)


# def printSum(num1, num2):
#     print(num1 + num2)
    
# printSum(10,20)
# printSum(20,40)



# aribtrary arguments

# when we are not sure about the number arguments that can be passed inside a function, add * to the parameter


# def myName(*name):
#     print('My name is ' + name[2])
#     print(name)


# myName('John', 'Peter', 'Raj')

# key words arguments
# we can send the aruguments in the form gor key = value

# def myName(name3, name1, name2):
#     print('My name is ' + name3)


# myName(name1='John',name2= 'Peter',name3= 'Raj')

# myName('John', 'Peter', 'Raj')

# arbitrary keyword arguments
# **kwargs


# def myName(**name):
#     print(name)
#     print( 'my name is ' + name["name2"])


# myName(name1='John',name2= 'Peter',name3= 'Raj')







# default parameter value
def myFunc(age = '40'):
    print('My age is ' + age)
    
myFunc('10')   
myFunc('20')   
myFunc()   

# default parameter value
# def myFunc(age = '40'):
#     print('My age is ' + age)
    
# myFunc('10')   
# myFunc('20')   
# myFunc()   

# Funstions either do something or returns something


# def printFruit(fruits):
#     print(fruits)
#     for fruit in fruits:
#         print(fruit)

# fruits = ['apples', 'bananas', 'oranges']
# printFruit(fruits)


# def printAge():
#     print(10)
#     print(10)
#     return 20
   
      


# print(printAge())

def myFunc(x):
    return 2*x
    
print(myFunc(5))
print(myFunc(6))


















































