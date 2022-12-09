def myFunc():
 a = 100
 print(a)

 
myFunc()


def myFunc():
 a = 100
 def insideFunc():
  print(a)
 insideFunc()

 
myFunc()


a = 100 #main body , global scope

def myFunc():
 print(a)  #local scope

 
myFunc()


def myFunc():

 def insideFunc():
  a = 100 

 insideFunc()

 

myFunc()
print(a)

a = 10

def myFunc():
 a = 20
 print(a)
 
myFunc()
print(a)
#scope

#you can access variable only from the region where it is created


a = 10

def myFunc():
 global a
 a = 20
 
 
myFunc()
print(a)