# Identity Operators


a = [10,20]

b = [10,20]

c = a

# print(a is c) # it will return true because a is the same object as c

# print(b is c) # it will return false although they have same values but not pointing to same memory location

# print( a == b) # it returns true because a is equal to b


# is not operator returns true if both variables are not the same object

print(a is not c)  #it returns false as a is the same object as c

print(b is not c) #it returns true because b is not the same object as c

print(a != b) # it returns false as a is equal to b

#Membership Operators

# These operators are used to test if a sequence is present or not in an object

a = [10,20,30,40]

print(20 in a)

print(20 not in a)

# in => it returns true if a sequence is present in an object
# not in => it returns true if a sequence is not present in an object

# BITWISE OPERATORS
# They are used to compare binary numbers

# & => AND => if both bits are 1, it sets each bit to 1 , otherwise 0

# | => OR => if one of the two bits is 1 , it sets each bit to 1 , otherwise 0

# ^ => XOR => if only one of the two bits is 1 , it sets each bit to 1

# ~ => NOT => complement operator, it returns one's complement of the number

# << => Zero fill left shift => the binary number is appended with 0's at the end

# >> => Right SHift => In simple terms, the right side of the bits are removed


x = 10
y = 7

print(x | y)
