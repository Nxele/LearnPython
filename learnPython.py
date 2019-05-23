print("Displaying Data from variables")
name = "sizwe"
surname = "Nxele"
Age = 24
print(name+" "+surname,Age)
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
three = float(3) # float 3.o will be display
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

xyz = abc.split(" ")
print(len(xyz)) #print arraySize

print("using the user input in Python")
print("enter a first number")
numberOne = input()
numberOne = int(numberOne)
print("enter a second number")
numberTwo = input()
numberTwo = int(numberTwo)
print("SUM OF TWO NUMBERS IS :",numberOne+numberTwo)

#working with modulus on python if remainder is Zero means even number else odd number
print("Enter a number")
number = input()
number = int(number)

numberIs = (number % 2)
if(numberIs >= 1):
    print("Entered number is a odd number")
else:
    print("Entered number is a even number")

print("Python logical operators")

opNum = 4
print( opNum > 2 and opNum < 10 ) #return true if both conditions are true
print( opNum > 2 or opNum <= 10) #return true if one condition is correct
print(not(opNum > 2 and opNum < 10)) # returns False because not is used to reverse the result

print("Python identity operator")

Ax = ["Sizwe","Nxele"]
Ay = ["Sizwe","Nxele"]
Az = Ax
#Returns true if both variables are the same object
print(Ax is Az) # returns True because Az is the same object as Ax
print(Az is Ay) # returns False because Ax is not the same object as Ay, even if they have thew same content
print(Ax == Ay) # to demonstrate the difference betweeen "is" and "==": this comparison returns True because Ax is equal to Ay

print(Ax is not Az) # returns false because Az is the same object as Ax
print(Az is not Ay) # returns True because Ax is not the same object as Ay, even if they have thew same content
print(Ax != Ay) # to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because Ax is equal to Ay

print("membership operator")

print("Sizwe" in Ax) #returns true if it finds sizwe on Ax Array (sequence)
print("Nduduzo" not in Ay) #return true because Nduduzo ls not in Array (sequence) Ay 

print("Python collection Array")

#A [[list]] is a collection which is ordered and changeable. In Python lists are written with square brackets.

thislist = ["apple", "banana", "cherry"]
print(thislist[1]) #print array value at index 1

#@ index 1 put new value
thislist[1] = "blackcurrant"
print(thislist)

#loop through the Array
for x in thislist:
    print(x)

#check if item is in the Array
if "apple" in thislist:
    print("Apple found in the Array")

#Array (collection) length
print(len(thislist))

#adding item at the end of the Array
thislist.append("lintch")
print(thislist[len(thislist)-1]) #displaying the last added record

#using insert() to add item on a specified index
thislist.insert(1,"orange")
print(thislist)

#using remove() to remove a specified item
thislist.remove("blackcurrant")
print(thislist)

#using pop() to remove item at a specified index
thislist.pop(1)
print(thislist)

#using del keyword to delete a index
del thislist[2]
print(thislist)

#del keyword could also be used to delete the Array completly 
# del thislist

#clear() method clears all the data inside the array
#thislist.clear()

#copying array using copy()
newlist = thislist.copy()
print(newlist)

#also ()list can be used to copy an list
mylist = list(newlist)
print(mylist)

#list() could also be used to create a list

oldlist = list((["Sizwe","Gugu","Mxo","Mino","Sisa","Aya"])) #node the double bracket
print(oldlist)

#count() count how many times the item appeared 
print(oldlist.count("Sizwe"))

#extends() used to add array items from another array or joining arrays
thislist.extend(oldlist)
print(thislist)

#index() find index number for a specific value (item)
print(thislist.index("Sizwe"))

#reverse() reverse the array order
thislist.reverse() #use use arrayName.sort(reverse = true)
print(thislist)

people = ["Sizwe","Aya","Mxo","Gugu","Siza","Mino"]

#sorting the Array
people.sort() 
print(people)

#can pass setting for the sort()
people.sort(reverse=True) #then false to sorting
print(people)

#sort() sort cars by length size
def myFunc(e):
    return len(e)
cars = ["Mercedes","BMW","VW","Porsche","Ford","Toyota"]
cars.sort(key = myFunc) #can also add reverse = true for reversing
print(cars)

def myFunA(e):
  return e['year']

car = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

car.sort(reverse=False,key=myFunA)
print(car)

#A ((tuple)) is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#you can also use the tuple constructort to create a tuple
newtuple = tuple(("Apple","Dell","HP","MSI"))
print(newtuple)
#on a tuple you can not add or remove data

#A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
thisset = {"Sizwe","Lebo","Mxo"}
print(thisset)

for index in thisset:
  print(index)

#on set we also use add() to add new data but once added data can't be removed
thisset.add("Gugu")
print(thisset)

#to add multiple data you use update
thisset.update(["Mino","Sisa","Aya"])
print(thisset)

#to remove data we use remove() and discard()
thisset.remove("Aya")
thisset.discard("Gugu")

#also pop is used to remove data since set are not unsordted you won't know which was deleted

deleted =  thisset.pop()
print(deleted)

#to clear all data in inside the set set.claer()
thisset.clear()

# del thisset() to delete the set
#also use set to create thisset = set(("Nxle","Nxumalo","Nxala"))

#A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

thisdiction = {"Brand":"BMW","Model":"//M3","Year":"2013"}
print(thisdiction)

#to access values inside dictionaries you use the key
print(thisdiction["Brand"])

#also you can use the get() method
print(thisdiction.get("Model"))

#to change the value upu specify the key name
thisdiction["Year"] = "1998"
print(thisdiction)

#this for loop print keys only
for index in thisdiction:
  print(index)

#to display values
for index in thisdiction:
  print(thisdiction[index])

#or specify values like:
for index in thisdiction.values():
  print(index)

#to loop through both value and key you use item
for x,y in thisdiction.items():
  print(x,y)

#Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdiction["Color"] = "Silver grey"
print(thisdiction)

#The pop() method removes the item with the specified key name:
thisdiction.pop("Model")

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdiction.popitem()

#delete item
del thisdiction["Year"]

# clear() to remove all data

#It is also possible to use the dict() constructor to make a new dictionary:
newdiction = dict(Model="",Year=2013,color="Grey")

#to copy we copy() and 

mydict = thisdiction.copy()
#or
mydict = dict(thisdiction)

#if | elif statements
print("enter a random number")
num = input()
num = int(num)

if(num > 0 and num <10):
  print("Entered number is lessthen 10")
elif(num > 10 and num <20):
  print("entered number is greater than 10")
else:
  print("number is greater than 20")

#short hand if is when you have one if you run it in one line

if(num > 50): print("Enter number is greater than 50")

#short hand if else
AA = 7
BB = 15
print("A class") if(AA < BB) else print("B class") 

#LOOPS Python have two primitive loop commands which are while (loop) and for (loop)

#while loop
#with the while loop we can execute as long as the statement condition is TRUE

i = 1
while(i < 10):
      print(i," ALL NUM")
      i += 1

#using break
iA = 1
while(iA < 7):
      print(iA," STOP @ 5")
      if(iA==5):
            break #can break the while loop b4 looging all items when you found what you are looking for
      iA +=1

#using continue
iE = 1
while iE < 5:
      iE += 1
      if iE == 3:
            continue #at index 3 we are saying skip number 3
      print(iE, " SKIP 3 & continue")

#THE RANGE FUNCTION IN FOR LOOP

for x in range(10):  #print range from zero to specified number
      print(x, "RANGE FROM 0 TO 10")

for x in range(2,5): #print range from start to end specified number default increment by 1
      print(x," Range from 2 To 5")

for x in range(5,25,5): #print using specified increment and start and end point (start,end,increment)
      print(x," Increment by 5 start-5 end 25")
#Nested Loops
adj = ["Red","Big","Tasty"]
fruit = ["Apple","Banana","Cherry"]

for x in adj:
      for y in fruit:
            print(x,y)

#Python functions also knowns as methods     
def my_function(): #creating a function
      print("I LOVE PROGRAMMINg (code killer)")

my_function() #calling my function

#information can be passed to a function as parameters 

def people_name(name):
      print(name+" Nxele")

people_name("Sizwe");
people_name("Mxolisi")
people_name("Gugu")

#use defaul parameter when parameter is not passed
def my_country(country = "South Africa"):
      print("I AM from :"+country)

my_country("Zimbabwe")
my_country()
my_country("Nigaria")

#return a value

def say_name(name):
      return name
print(say_name("Sizwe Nduduzo Nxele"))

#Recursion in python means calling a function within functions

def tri_recursion(k):
      if(k>0):
            result = k+tri_recursion(k-1)
            print(result)
      else:
            result = 0
      return result
tri_recursion(6)

#Lambda expression in python
#A lambda function can take any number of arguments, but can only have one expression.
xXx = lambda a : a + 10
print(xXx(5))

#a lambda expression that takes two numbers 
v = lambda a,b: a * b
print(v(5,5))

# a lamba expression that sums up three number
s = lambda f,t,e: f + t + e
print(s(5,10,11))

#Use that function definition to make a function that always doubles the number you send in:
def myfunc(n):
      return lambda a : a * n

mydoubler = myfunc(2) #specifies that the passed number must be doubled
mytrippler = myfunc(3) #specifies that the passed number must be tripled

print(mydoubler(11)) #the passed number
print(mytrippler(5)) #the passsed number

#classes in Python
class human: #creating a class called human
      def __init__(self,name,surname,age,counrty,occupation): #creating a constructor
            self.name = name #assign value to the class blue print or object
            self.surname = surname
            self.age = age
            self.country = counrty
            self.occupation = occupation

      def show_person(self):
            print(self.name,self.surname,self.age,self.country,self.occupation)

person = human("Sizwe","Nxele",24,"South Africa","Developer") #creating an object for a parameterised constructor
person.show_person() #calling a method inside using class object

person.name = "Nduduzo" #you can modify person object data

del person.country #you can delete person property

del person #you can also delete the object

person.show_person() #calling person again after deleting data

"""class carLove:
      def __init__(bmw,model,year,color):
            bmw.model = model
            bmw.year = year
            bmw.color = color

      def printCars(cars):
            print(cars.model,cars.year,cars.color)

mycar = carLove("BMW //M3",2013,"silver")
mycar.printCars()"""



