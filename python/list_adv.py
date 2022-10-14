# List Sorting

# Sort in alpha numeric order default it is ascending


# my_list = ['banana', 'orange', 'apple', 'guava' ]
# my_list = [90, 400, 200 , 20 , 10 , 50 ]
# my_list.sort()

# print(my_list)


# sort in descending order

# my_list = [90, 400, 200 , 20 , 10 , 50 ]
# my_list.sort(reverse = True)

# print(my_list)


# Case Insensitive sorting
# by default sort() is case-sensitive
# all the capital letters will be sorted before lowercase letters
my_list = ['banana', 'Orange', 'Apple', 'guava' ]

# my_list.sort(key = str.lower)

# print(my_list)


# reverses the order of a list
# my_list = ['banana', 'orange', 'apple', 'guava' ]

# my_list.reverse()

# print(my_list)

# Copying the list

list1 = [10,20,30,40] #original list

# list2 = list1.copy() #copy list

list2 = list(list1) #another way for copying of the list

print(list2)

list2.pop()
print(list1)
print(list2)



















