# inheritance, polymorphism, encapsulation, abstraction

# class is a collection of objects

# Inheritance
# parent => child class
# single inheritance, multilevel , multiple

# class Car:
#     def __init__(self, modelname, year):
#         self.modelname = modelname
#         self.year = year

#     def displayCar(self):
#         print(self.modelname, self.year)


# car1 = Car("Maruti", 2018)
# car1.displayCar()

# polymorphism
# many form
# same function name

# inbuilt function
# print(len('abc'))
# print(len([10, 20, 30, 40]))

# custom polymorphism
# def sum(a, b, c=0):
#     return a + b + c


# print(sum(10, 20))
# print(sum(10, 20, 30))

# polymorphism classes


# class India():
#     def language(self):
#         print('Hindi is our official language')


# class Canada():
#     def language(self):
#         print('French is our official language')


# india_obj = India()
# canada_obj = Canada()

# for country in (india_obj, canada_obj):
#     country.language()

# polymorphism in inheritance

# encapsulation

# bundling properties and methods into one single unit
# combine properties and methods into a single unit so that
# they are not accessible outside of the class

# public members(access them within and outside of the class)
# protected members(access them within the class and sub class)
# private members(access them within class itself)

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name #public member
#         self._project = project  #protected member
#         self.__salary = salary  #private


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name  # public member
#         self.__salary = salary  # private member

#     def empDetails(self):
#         print('Name ', self.name, 'Salary ', self.__salary)


# employee1 = Employee('John', 20000)
# # print('Salary of this employee is ', employee1.name)
# employee1.empDetails()

# parent class or base class
class Company:
    def __init__(self):
        # protected member
        self._project = "AI"

# child class


class Employee(Company):
    def __init__(self, name):
        self.name = name
        Company.__init__(self)

    def showDetails(self):
        print("Employee name: ", self.name)
        # access the protected member
        print("Working on a project :", self._project)


emp1 = Employee('John')
emp1.showDetails()
print('Project: ', emp1._project)


# security => preventing the unauthorised access to objects
# data hiding
# simplifies by keeping the classes separate
# more readable and maintainable
