#income = int(input("Enter income: "))

#if income < 7000:
#    print("Scholarship is available")
#else:
#    print("Not eligible for scholarship")

#---------------------------------------#

# num = int(input("Enter a number: "))

# if num % 3 == 0 and num % 5 == 0:
#     print("the number is divisible by 3 and 5")
# else:
#     print("the number is not divisible by 3 and 5")

#---------------------------------------#

# a = int(input("Enter the score:"))

# if(a < 35):
#     print("Poor Student")
# elif(a > 35 and a < 70):
#     print("Average Student")
# elif(a > 70 and a < 100):
#     print("Good Student")
# else:
#     print("Invalid score")

#---------------------------------------#

# salary = int(input("Enter salary: "))
# age = int(input("Enter age: "))

# if salary >= 20000 or age <= 25:
#     loan = int(input("Enter required loan amount: "))
#     print("Loan amount entered:", loan)
# else:
#     print("Not eligible for loan")

#---------------------------------------#

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# choice = input("Enter operation (add/sub/mul/div): ")

# if choice == "add":
#     print("Result:", a + b)
# elif choice == "sub":
#     print("Result:", a - b)
# elif choice == "mul":
#     print("Result:", a * b)
# elif choice == "div":
#     print("Result:", a / b)
# else:
#     print("Invalid operation")

#---------------------------------------#

per = int(input("Enter percentage: "))

if per >= 70:
    name = input("Enter name: ")
    dept = input("Enter department: ")
    location = input("Enter location: ")
    print("You are eligible")

else:
    print("You are not eligible")