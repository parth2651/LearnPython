# install Python on windows and Mac
# install linter - pylint
# install code formatter use "Format Document" command in programm
# set format on save in setting to true
# install code runner
# ctrl +  tilda for terminal
# ctrl + shift + P for program or command


# basic print to test after installation
print("Parth Patel")
print("*" * 10)
print("this is test")

'''some concept about python 
its created in c so its cpythin there is jython for Java,  ironpython for c#
you can use c# code in that - it complies in to kind o MSIL or JIT - never tried but good to know
'''
# Python is dynamic language no need to define type it will take automatically '
x = 1
y = "string"


# each data type is class like below'
print(type(x))
print(type(1.1))
print(type(True))
print(type("parth"))


# to get each memory locatoin
# there is default function id(x)
print(id(x))
print(id(y))
print(id("Parth"))


# for each mutable type python will add new memory location
x = 1
print(id(x))
x = x+1
print(id(x))
# for each mutable type python will keep its same memory location
x = [1, 2, 3]
print(id(x))
x.append(4)
print(id(x))


# strings
course = "python programming"
print(len(course))
print(course[0])
print(course[-1])  # nagaive index goes back of the string
# split string
# note: it doesn;t include last index so it will return index 0, 1 and 2
print(course[0:3])
print(course[:3])
print(course[0:])


# escape sequence
course = "python programming"
# use either single quot
# \"
# \'
# \\
# \n - advise to use '''
course = 'python "programming'
print(course)
course = "python \"programming"
print(course)
course = "python \\\"programming"
print(course)


# formater
firstname = "Parth"
Lastname = "Patel"
# oldschool
fullname = firstname + " " + Lastname
print(fullname)

# this is formatter f"" or F""
fullname = f"{firstname} {Lastname}"
print(fullname)

# you can do any valid expression in formatter
fullname = f"{firstname} {Lastname} {len(firstname)} {2 + 2}"
print(fullname)


# string mehods
print(fullname.upper())
print(fullname.lower())
print(fullname.title())
# trim = strip, lstri,  rstrinp
print(fullname.strip())
# index of = find, returns first index and its case sensitive
print(fullname.find("at"))
print(fullname.replace("P", "-"))
# below is kind of contains and return True/False
print("parth" in fullname)
print("Parth" in fullname)


# numbers
x = 10
# binary represantation of 10 represanted with 0b
x = 0b10
print(x)
# to binary represantation of any number use bin()
print(bin(x))
print(bin(2))

# hexa decimal
x = 0x12c
print(x)
# to hex represantation of any number use hex()
print(hex(x))
print(hex(300))

# complex number - we are not going to use this but FYI
x = 1+2j
print(x)


# artithmatic operation
x = 10 + 3
x = 10 - 3
x = 10 * 3
# normal division return decimal
x = 10 / 3
print(x)
# rounded division return non decimal
x = 10 // 3
print(x)
x = 10 % 3
print(x)
x = 10 ** 3
print(x)
# there is not x++ or Y-- its either x = x + 1, x += 1


# working with numbers
# import math
# and lot of functions like math.floor etc


# type conversation
x = input("x: ")
y = x+1
