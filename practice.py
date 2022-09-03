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

x = 50

def func():
    global x
    print('This function is now using the global x!')
    print('Because of global x is: ', x)
    x = 2
    print('Ran func(), changed global x to', x)

print('Before calling func(), x is: ', x)
func()
print('Value of x (outside of func()) is: ', x)
