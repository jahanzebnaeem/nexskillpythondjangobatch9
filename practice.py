# 1st variation of function
# def my_addition():
#     """
#     Input param: None
#     Does: add 2 values
#     Output: print values
#     """
#     print(2+2)
#
# my_addition()

# 2nd variation of function
# def my_addition(oprend1, oprend2):
#     print (oprend1+oprend2)
#
# my_addition(4, 6)

# 3rd variation of function
# def my_addition(oprend1, oprend2):
#     return (oprend1+oprend2)
#
# print(my_addition(4, 6))

# Scope
# x = 25
#
# def printer():
#     x = 50
#     return x
#
# print(x)
# print(printer())

# def greet():
#     # Enclosing function
#     name = 'Sammy'
#
#     def hello():
#         print('Hello '+name)
#
#     hello()
#
# greet()

# x = 50
#
# def func(x):
#     print('x is', x)
#     x = 2
#     print('Changed local x to', x)
#
# func(x)
# print('x is still', x)

# x = 50
#
# def func():
#     global x
#     print('This function is now using the global x!')
#     print('Because of global x is: ', x)
#     x = 2
#     print('Ran func(), changed global x to', x)
#
# print('Before calling func(), x is: ', x)
# func()
# print('Value of x (outside of func()) is: ', x)

# x = 25
#
# def printer():
#     x = 50
#     return x
#
# print(x)
# print(printer())
# print(x)

# name = 'This is a global name'
#
# def greet():
#     # Enclosing function
#     name = 'Sammy'
#
#     def hello():
#         print('Hello '+name)
#
#     hello()
#
# greet()

# l = [1,2,3]
#
# print(l.count(2))

# print(type(()))

# class Sample():
#     pass
#
# x = Sample()
#
# print(type(x))

# class Dog():
#     species = 'mammal'
#
#     def __init__(self,breed,name):
#         self.breed = breed
#         self.name = name
#
# sam = Dog(breed='Labrador', name='sam')
# # tommy = Dog(breed='Huskie')
#
# # sam.breed = 'Kuchb'
#
# print(sam.breed)
# print(tommy.species)

# class Circle():
#     pi = 3.14
#
#     # Circle get instantiated with a radius (default is 1)
#     def __init__(self, radius=1):
#         self.radius = radius
#
#     # Area method calculates the area. Note the use of self.
#     def area(self):
#         return self.radius * self.radius * Circle.pi
#
# c = Circle()
#
# print(c.area())

# class Animal():
#     def __init__(self):
#         print ("Animal created")
#
#     def whoAmI(self):
#         print ("Animal")
#
#     def eat(self):
#         print ("Eating")
#
# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         print ("Dog created")
#
#     def whoAmI(self):
#         print ("Dog")
#
#     def bark(self):
#         print ("Woof!")
#
# d = Dog()
# d.whoAmI()
# d.eat()
# d.bark()
# print(d)

class Book():
    def __init__(self, title, author, pages):
        print ("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title:%s , author:%s, pages:%s " %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print ("A book is destroyed")

book = Book("Python Rocks!", "Jahanzeb Naeem", 159)

#Special Methods
print(book)
print (len(book))
del book
