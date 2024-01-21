# Two ways of creating a list

#1st way
language = 'Python'
lst = list(language)
print(type(lst))
print(lst)

#2nd way
lst = [i for i in language]
print(type(lst))
print(lst)


# Generating numbers

# numbers
numbers = [i for i in range(11)]
print(numbers)

# mathematical operations
squares = [i * i for i in range(11)]
print(squares)

# list of tuples
numbers = [(i, i * i) for i in range(11)]
print(numbers)

# even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)

# Odd numbers
odd_numbers = [i  for i in range(21) if 1 % 2 != 0]
print(odd_numbers)

# Filter numbers
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [ i for i in range(21) if i % 2 == 0 and i > 0]
print(positive_even_numbers)

# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)


# Lambda function
x = lambda param1, param2, param3: param1 + param2 + param2
# print(x(arg1, arg2, arg3))

# Named function
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))

# Function changed to Lambda function
add_two_nums = lambda a, b : a + b
print(add_two_nums(2,3))

square = lambda x : x ** 2
print(square(3))
cube = lambda x : x ** 3
print(cube(3))

# Multiple variables
multiple_variables = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variables(5, 5, 3))

# Lambda  function inside another function
def power(x):
    return lambda n : x ** n


cube = power(2)(3)
print(cube)
two_power_of_five = power(2)(5)
print(two_power_of_five)
