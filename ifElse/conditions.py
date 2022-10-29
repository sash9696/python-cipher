# if else conditions

# some imp logical conditions

# Equals x == y
# Not Equals x != y
# less than x < y
# greater than x > y
# less than equal x <= y
# greater than equal x >= y



# if(condition):
#     code if the condition is true
# x = 5
# y = 10
# # if( x < y ):
# #     print('20 is greater than 10')

# if(x > y):
#     print('x is greater than y')
# else: #rest of the condition will be executed except the if the part
#     print('x is equal to or less than y')

# student can only enter the college if student enter time is less than college entry time
# if student comes at college entry time then student is allowed but with late remarks
collegeEntryTime = 9
studentEnterTime = 13

if(studentEnterTime < collegeEntryTime):
    print('you can enter in the college')
elif(studentEnterTime == collegeEntryTime):
    print('you can enter with late remarks')
elif(studentEnterTime > 12):
    print('allowed to enter in the college with proper felicitation')
else:
    print('go back to hostel')


# short hand if condition

# # if(10>5): print('10 is greater than 5')

# # short hand if-else condition

# # x = 20
# # y = 10

# # print('X') if x > y else print('Y')


# # and and or keywords. , logical operators

# x = 40
# y = 20
# z = 30

# # if(x < y and x < z):
# #     print('both the conditions are true')

# if(x < y or x < z):
#     print('If any one of the condition is true')


# nested conditions

age = 18

if( age < 18):
    print('age is less than 18')
    if(age < 10):
        print('the person is a minor. no entry allowed')
    else:
        print('the person is allowed') #range for this else is 10-17
else:
    print('age is greater than or equal to 18')





















