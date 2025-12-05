# def hello_world():
#     return "Hello, World!"

# print(hello_world())

# ---------------------------------------------------------

# def sum(num1,num2):
#     return num1+num2

# print(sum(7,5))

# ---------------------------------------------------------

# def do_nothing():
#     pass

# print("do_nothing function")
# do_nothing()

# ---------------------------------------------------------

# def sum(num1, num2):
#     if type(num1) is not int or type(num1) is not int:
#         return 
#     return num1 + num2

# print(sum(4,5))
# print(sum(10.4, 5))
# print(sum("4", 5))
# print(sum(4, b))

# ---------------------------------------------------------

# def multiple_items(*args):
#     print(args)
#     print(type(args))


# multiple_items(1,2,3,4,5)
# multiple_items("apple", "banana", "cherry")
# multiple_items(1, "apple", 3.14, True)
# multiple_items()  # No arguments passed

# ---------------------------------------------------------

# def add(*num):
#     sum = 0
#     for n in num:
#         sum += n
#     print("Sum:", sum)

# add(1,2,3)
# add(10,20,30,40,50)
# add()  # No arguments passed

# ---------------------------------------------------------

# def multi_named_items(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

# multi_named_items(name="Alice", age=30, city="New York")
# multi_named_items(product="Laptop", price=999.99, stock=50)
# multi_named_items()  # No arguments passed

# ---------------------------------------------------------

# def func(a,b,*args,option=False,**kwargs):
#     print(' ')
#     print(a,b)
#     print(args)
#     print(option)
#     print(kwargs)

# func(1,3,10,20,Name="Nazia",salary=60000)

# ---------------------------------------------------------

# def func(a,b,args,option=False,*kwargs):
#     print(' ')
#     print(a,b)
#     print(args)
#     print(option)
#     print(kwargs)


# func(1,3,10,20,Name="Virat",salary=92000)

# ---------------------------------------------------------

# print("usage of default values")
# def func1(a,b=4):
#     print(' ')
#     print(a,b)

# func1(1,7)


# ---------------------------------------------------------

# def add_one(num):
#     if(num>=9):
#         return num+1
#     total = num+1
#     print(total)
#     return add_one(total)

# mynewtotal = add_one(0)
# print(mynewtotal)


# ---------------------------------------------------------

# prog to print factorial of anumber recursively

# recursive function

# def recursive_factorial(n):
#     if n==1:
#         return n
#     else:
#         return n*recursive_factorial(n-1)
    
# # user input
# num = 6

# if num<0:
#     print("Invalid input! please enter a positive number")
# elif num == 0:
#     print("factorial of number 0 is 1")
# else:
#     print("factorial of number", num, "-", recursive_factorial(num))

# ---------------------------------------------------------

# Function exercise

# Q1.Create a function called add(), sub(), mul(), div() and 
# get the input for a and b inside every function then print the result.

# def add():
#     a = float(input("Enter value for a: "))
#     b = float(input("Enter value for b: "))
#     print("Addition =", a + b)

# def sub():
#     a = float(input("Enter value for a: "))
#     b = float(input("Enter value for b: "))
#     print("Subtraction =", a - b)

# def mul():
#     a = float(input("Enter value for a: "))
#     b = float(input("Enter value for b: "))
#     print("Multiplication =", a * b)

# def div():
#     a = float(input("Enter value for a: "))
#     b = float(input("Enter value for b: "))
#     if b == 0:
#         print("Cannot divide by zero")
#     else:
#         print("Division =", a / b)


# add()
# sub()
# mul()
# div()



# ---------------------------------------------------------

# Q2.Get an integer number from user and pass it to the 
# function called findeveorodd(). Let the function print whether number is even or odd.

# def findeveorodd(num):
#     if num % 2 == 0:
#         print(num, "is Even")
#     else:
#         print(num, "is Odd")


# n = int(input("Enter an integer: "))
# findeveorodd(n)


# ---------------------------------------------------------

# Q3. Get input for a and b and pass it to the function 
# called printrange(). Let the function print numbers from a to b.

# def printrange(a, b):
#     for i in range(a, b + 1):
#         print(i, end=" ")
#     print()


# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# printrange(a,b)