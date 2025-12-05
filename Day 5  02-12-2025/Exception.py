# following are some examples of runtime errors in Python

# print(c)

# prin(c)

# nameError , ValueError , TypeError , ZeroDivisionError , IndexError , KeyError , AttributeError

# to avoid runtime errors we use exception handling

# ******************************************************************************

# Exception Handling

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     print("Result:", a + b)

# except Exception as e:
#     print("Something went wrong! ", e)

# ******************************************************************************

# try:
#     a = input()
#     b = input()
#     print(a / b)
    
# except Exception as e:
#     print("Something went wrong! ", e)

# ******************************************************************************

# try:
#     a = int(input("Enter a number: "))

# except ValueError as e:
#     print("ValueError occurred: ", e)

# *****************************************************************************

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     c = input()
#     print(c/a)
#     print(d)

# except ValueError as ve:
#     print("ValueError occurred: ", ve)

# except TypeError as te:
#     print("TypeError occurred: ", te)

# except Exception as e:
#     print("Some other exception occurred: ", e)

# finally:
#     print("Done")

# ******************************************************************************

# try:
#     print(x)

# except NameError:
#     print("NameError occurred means something is not defined")

# ******************************************************************************

# x=10
# try:
#     # print(x/1)
#     # print(x/0)
#     # print(y)

# except ZeroDivisionError as zde:
#     print("Please don't divide by zero ")

# except Exception as e:
#     print("Some other exception occurred: ", e)

# else:
#     print("No exception occurred")

# finally:
#     print("I am always executed")

# ******************************************************************************

