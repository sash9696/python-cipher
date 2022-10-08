

# listItems = [10,20,30,40]
# listItems = [10,20,30,40, 'apples', 'oranges']
listItems = [10,20,30,40, 40, 30]

print(listItems[6])
# print(listItems)
# print(type(listItems))



# listOne = ['abcd', 40, True, 60, 'apples']

#creating a list through constructor

listOne = list((10,20,30))
listTwo = [10,20,30]


print(listOne)
print(listTwo)


#access items of a list

list1 = [10,20,30,40,50]

# print(list1[-2])

# search will start at index 2(include) and end at index 5(not included)
# print(list1[2:5])

# print(list1[:4])

# print(list1[2:])

# change the list items

# list1 = [30,60,10,20,80]

# list1[1] = 90
# list1[2] = 'hello'

# print(list1)

#change a range of list items
# list1[1:3] = ["hi", "hello"]

# if you insert more items than replace then new items will be inserted at the index that we provided
list1 = [10,20,30]
list1[1:2] = ["hi", "hello"]
print(list1)
# adding the list items

# insert items

# list1 = [10,20,30]

# list1.insert(2, 40)
# print(list1)

# append items
# for adding the item at the end of the list
# list1 = [10,20,30]

# list1.append(40)
# list1.append(50)
# list1.append(60)
# print(list1)


#extend a list
# To append or to add elements from another list into the current list we use extend()
#you can add or append any kined of iterable objects like tuples, sets, dictionaries etc.

list1 = [10,20,30]
# list2 = [40,50,60]
tuple = (50,60)
# list1.extend(list2)
# print(list1)
# print(list2)
list1.extend(tuple)
print(list1)


# remove a specified item from the list
# remove()

# myList = ['john', 'peter', 'raj']
# myList.remove('raj')
# print(myList)

#remove item from specified index

myList = ['john', 'peter', 'raj']
# myList.pop(2)


# removing last item
# myList.pop()
# myList.pop()
# myList.pop()
# print(myList)



#remove item from specified index using del keyword

# myList = ['john', 'peter', 'raj']

# # del myList[0]
# del myList
# print(myList)

#empty the list

myList = ['john', 'peter', 'raj']
myList.clear()
print(myList)
