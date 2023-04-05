import math
# write a function to calculate
# area and perimter of a rectangle


# def rectangle_info():
#     length = float(input("Enter the length of the rectangle: "))
#     width = float(input("Enter the width of the rectangle: "))

#     area = length * width
#     perimeter = 2 * (length + width)

#     print(f'The area of {length} and {width} is: {area}, and the perimeter is: {perimeter}')
# rectangle_info()


# Python program to display the Fibonacci sequence

# def fib(n):
#     x = 0
#     y = 1
#     print(x)
#     print(y)

#     for i in range(3, n):
#         z = x + y
#         print(z)
#         x = y
#         y = z
#         z = x + y
# terms = int(input('Enter the number of terms: '))
# fib(terms)


# write a function that accepts a number and prints its factorial


def factorial():
    enter = int(input('Enter a number to check the factorial: '))
    print(f'The factorial of {enter} is: {math.factorial(enter)}')


factorial()


# def factorial():
#     n = int(input('Enter a number: '))

#     factorial = 1

#     if n >= 1:

#         for i in range(1, n+1):

#             factorial = factorial * i
#             print(factorial)


# print(f'Factorial of the given number is: ', factorial())
