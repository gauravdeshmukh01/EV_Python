# squared = lambda num: num * num
# print(squared(5))

# add_two = lambda num: num + 2
# print(add_two(8))

# sum_total = lambda a, b: a + b
# print(sum_total(36, 69))

#***************************************************************************

# def funcBuilder(x):
#     return lambda num: num + x

# add_ten = funcBuilder(10)
# add_twenty = funcBuilder(20)

# print(add_ten(7))
# print(add_twenty(7))

#***************************************************************************

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # squared_numbers = list(map(lambda num: num * num, numbers))
# # print(squared_numbers)
# # OR
# squared_numbers = map(lambda num: num * num, numbers)
# print(list(squared_numbers))


# # even_numbers = list(filter(lambda num: num % 2 == 0, numbers))
# # print(even_numbers)
# # OR
# even_numbers = filter(lambda num: num % 2 == 0, numbers)
# print(list(even_numbers))

#***************************************************************************

# from functools import reduce

# numbers = [1, 2, 3, 4, 5,6,7,8,9,10]

# total = reduce(lambda acc, curr: acc + curr, numbers)
# print(total)

# print(sum(numbers))

#***************************************************************************

from functools import reduce

names  = ["Alice", "Bob", "Charlie", "David", "Eve"]

char_count = reduce(lambda acc, name: acc + len(name), names, 0)
print(char_count)