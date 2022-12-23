# reading a file
# file = open('/Users/harshitchopra7/Desktop/Python/test/hello.txt')

# print(file.read())

# read a part of the file

# file = open('test/hello.txt')
# print(file.read(7))

# file = open('test/hello.txt', 'r')
# # print(file.readline())
# # print(file.readline())
# for line in file:
#     print(line)

# file.close()

# file.readline()


# write or create the files
# 'a' => append = will add to the end of the file
# file = open('test/hello.txt', 'a')
# file.write('Added extra text in the end')
# file.write('more extra text')

# file.close()

# file = open('test/hello.txt', 'r')
# print(file.read())

# 'w' => write = will overwrite  existing content
# file = open('test/hello.txt', 'w')
# file.write('Removed existing text and added new')
# file.close()

# file = open('test/hello.txt', 'r')
# print(file.read())


# create the files

# "x" => create - creates new file and return an error if file is
#  'w' => write =creates the file if file doesnt exist
#  'a' => write = creates the file if file doesnt exist

# file = open('newFile.txt', "x")
# file = open('newFile.txt', "a")
# file = open('newFile.txt', "w")


import os

# os.remove('test/hello.txt')

# if os.path.exists('text/hello.txt'):
#     os.remove('test/hello.txt')
# else:
#     print('The file does not exist')


# os.rmdir('test')
# you can only remove empty folders
