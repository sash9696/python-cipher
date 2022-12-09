
newTuple = (10,20,30)
myiter = iter(newTuple)

print(next(myiter))
print(next(myiter))
print(next(myiter))


newStr = 'python'
newIter = iter(newStr)

print(next(newIter))
print(next(newIter))

print(next(newIter))

print(next(newIter))


#iterators is an object on which you can traverse upon

#lists, tuples, dictionaries are iterable objects

newTuple = (10,20,30)
newStr = 'python'

for num in newTuple:
 print(num)
 
for char in newStr:
 print(char)