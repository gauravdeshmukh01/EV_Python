# for i in "apple":
#    print(i)

# for i in range(1,5):
#    print(i)

# for i in range(11):
#    print(i)

# ------------------------------------------------ 

# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))

# for i in range(a+ 1, b):
#     print(i)

# ------------------------------------------------    

# for i in range (1,11):
#     print(i, "x2=", i*2)

# ------------------------------------------------

# even or not

# for i in range (1, 11):
#     if i % 2 == 0:
#         print(i, "is even")
#     else:
#         print(i, "is odd")

# ------------------------------------------------

# cnt = 0
# for i in range(1, 11):
#     if i%2!=0: cnt += 1
# print(cnt)

# ------------------------------------------------

# Count numbers divisible by both 3 and 5 (Range 1–100)

# count = 0
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         count += 1

# print("Count:", count)

# ------------------------------------------------

# Sum of the first 5 natural numbers

# total = 0
# for i in range(1, 6):
#     total += i

# print("Sum:", total)

# ------------------------------------------------

# Read 10 numbers and find their sum and average

# total = 0

# for i in range(10):
#     num = float(input("Enter number: "))
#     total += num

# average = total / 10

# print("Sum:", total)
# print("Average:", average)

# ------------------------------------------------

# Nested loops: Print weeks and days

# for i in range(1,3):
#     print("Week:", i)
#     for j in range(1, 4):
#         print("  Day:", j)

# ------------------------------------------------

for i in range(1, 5):     
    for j in range(1, i+1):   
        print(j, end=" ")
    print()