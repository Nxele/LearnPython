print("Displaying Data from variables")
name = "sizwe"
surname = "Nxele"
Age = 24
print(name,surname,Age)
print("if statement and inednting use case")

if( 5 > 2):
    print('Five is greater than Two')
if(2 < 5):
    print('Two is less than Five')
#This is a comment is python

""" Docstring this is used to comment a block of code in python"""
print("getting viriable data type")

x = "Sizwe" #String
y = 'Nxele' #String
a = 24 #int
b = 2.8 #float
z = 1j #complex

print(type(x))
print(type(y))
print(type(a))
print(type(b))
print(type(z))

print("specifying data type in Python Casting")

one = int(1) # interger 1 
two = int(2.8) #integer 2 will be display 
three = float(3); # float 3.o will be display
four = str('Sizwe')
five = str(5.0)

print(one,type(one))
print(two,type(two))
print(three,type(three))
print(four,type(four))
print(five,type(five))

print(four+" ",one) #to concatinate numbers you use a comma(,) and a plus sign for Strings (+)

print("Python String Literals (string in an array of characters it have references)")

abc = "Sizwe Nduduzo Nxele"
print(abc[4]) #displaying one character
print(abc[2:5]) #diaply characters from 2-5 on abc
print(abc.strip()) #removes any white spaces at the beggining or at the end
print(len(abc)) #returns the length of the String
print(abc.lower()) #convert object to lowecase
print(abc.upper()) #convert object to uppercase
print(abc.replace("Sizwe","Microvecter")) #replace object data with new data
print(abc.split(" ")) #split an object to an Array using provided character

print("using the user input in Python")
print("enter a first number")
numberOne = input()
numberOne = int(numberOne)
print("enter a second number")
numberTwo = input()
numberTwo = int(numberTwo)
print("SUM OF TWO NUMBERS IS :",numberOne+numberTwo)