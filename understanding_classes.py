#Write a class called Address that has two attributes: number and street_name
 
class Address(object):
    def __init__(self, street, num):  ##initializing the object = saying what attributes are under this class
                                        ##ie, what are addresses made of? a street name and number
        self.street_name = street  ##the attribute is street_name
        self.number = num  ##the attribute is number
 
##Imagine that 'self' is replaced with Address. Street_name and number methods
##that can work with Address class. Just as append works with the list "class".
 
##Another example
 
class Song(object):
    def __init__(self, lyrics):   ##initializing the object = what attributes are under this class?
                                ## ie, what are songs made of? lyrics. 
        self.lyrics = lyrics     ##the attribute is lyrics
 
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
 
happy_bday = Song(["Happy birthday to you",     #The 'Song(blah)' here is like saying 'str(blah)'
                   "I don't want to get sued",
                   "So I'll stop right there"])
 
bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])
 
happy_bday.sing_me_a_song()
 
bulls_on_parade.sing_me_a_song()
 
#This prints out the song. 
 
#Analogy
'''
class String(object):
    def __init__(self, word):
        self.string = word

    def lower(string/self):
        for letter in word:
            x = letters changed to lowercase
            print x

test = string(JANEY)
test.lower() ---> janey
This is just like saying, Janey (the object), print yourself!

'''
 
 
##For dictionaries- "Key" and "value" are methods, dictionary is the class, and specific
##dictionaries are instances of the class dictionary.
 
#Exercise 3.6 - Queue is first-in-first-out
print "Class queue starts here"
 
class Queue(object):
 
    def __init__(self):
        self.items = []
 
    def insert(self, item):
        self.items.append(item)
 
    def remove(self):
        if self.items:
            self.items.pop(0) #0 because you remove the thing that has been there the longest
            print 
        else:
            print "The queue is empty"
 
#Exercise 3.7 - Stack is last-in-first-out
class Stack(object):
 
    def __init__(self):
        self.items = []
 
    def insert(self, item):
        self.items.append(item)
 
    def remove(self):
        if self.items:
            self.items.pop()
            print
        else:
            print "The queue is empty"
 
#Another example
class Employee(object):
    empCount = 0 #this is a class variable that remains throughout the entire class
 
    def __init__(self, name, salary): #if you initialize this class, you will put name
    #and salary in the parentheses as arguments. called the CLASS CONSTRUCTOR
        self.name = name 
        self.salary = salary
        Employee.empCount += 1 #if you initialize this class (ie use Employee(smt,smt))
        #the count will go up by 1
 
    def displayCount(self):
        print Employee.empCount
        #if you say somevariable.displayCount(), it will print the count, no matter what that variable is
 
    def displayEmployee(self):
        print self.name, self.salary
        #if you say somevariable.displayEmployee(), it will print that variable's name and salary
 
emp1 = Employee("Zara", 2000)
#This creates an INSTANCE of class Employee
emp2 = Employee("Manni", 5000)
#this creates the second instance of class Employee
print Employee.empCount
#we entered two employees, so the count went up to 2
 
 
#Another Example
class Shape(object): 
    def __init__(self, x, y): #When you make an instance of this class, you will
    #enter Shape(xvaluehere, yvaluehere)
        self.x = x 
        self.y = y
    description = "shape has not been described yet"
 
    def area(self):
        return self.x * self.y
    def perimeter(self):
        return 2*self.x * 2*self.y
    def describe(self,text):
        return text #Here you give it a description 
    def scaleSize(self,scale):
        self.x = self.x * scale
        self.y = self.y * scale 
 
rectangle = Shape(100,45) #create rectangle with parameters 100 and 45
print rectangle.area() #find the area
print rectangle.perimeter() #find the perimeter
print rectangle.describe("A wide rectangle")
rectangle.scaleSize(0.5) #make rectangle 50% smaller
print rectangle.area() #print area of new smaller rectangle
 
#Now let's create a class that inherits from Shape
 
class Square(Shape):  #in parens, put class you are inheriting from
    def __init__(self,x):
        self.x = x
        self.y = x
#inherited everything from shape class that's the same, but changed just
#self.x and self.y
 
# How about another child class for a double square? The shape looks like this:
# _________
#|    |    |
#|    |    |
#|____|____|
 
class DoubleSquare(Square):
    def __init__(self,y):
        self.x = 2*y
        self.y = y
    def perimeter(self):
        return 2*self.x + 2*self.y
    def area(self):
        return self.x * self.y * 2
 
janey = DoubleSquare(3)
print janey.area()
