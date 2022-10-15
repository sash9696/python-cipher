

# tuple1 = (10,20,30)

# del tuple1

# print(tuple1)

# unpack a tuple
# in python, we can extract the values into diff varibales. This is unpacking

# numbers = (10,20,30) #packing

# (num1, num2, num3) = numbers # num of variables should match number of items in tuple

# print(num1)
# print(num2)
# print(num3)

numbers = (10,20,30,40,50,60,70,80) #packing

# (num1, num2, *num3) = numbers # num of variables should match number of items in tuple

(num1, *num2, num3) = numbers # num of variables should match number of items in tuple

print(num1)
print(num2)
print(num3) #rest of the values are stored in a list

# Loop Through Tuples

# for loop

myTuple = ('apples', 'banana', 'orange')
# for x in myTuple:
#     print(x)

# looping through index numbers

# for i in range(len(myTuple)):
#     print(myTuple[i])


# Joining tuples

tuple1 = (10,20,30,40)
tuple2 = (50,60,70,80,90)

tuple3 = tuple1 + tuple2

# print(tuple3)

# multiplcation of tuples

myTuple = ["apple", "oranges", "banana"]

multipliedTuple = myTuple * 3

print(multipliedTuple)