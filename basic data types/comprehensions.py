# List Comprehensions
values = [x for x  in range(10)]
print(values)
values1 = [x +1 for x in range(10)]
print(values1)

# Get even numbers from 0 to 50
evenNumbers = [x for x in range(50) if x %2 == 0]
print(evenNumbers)

# String Comprehensions
options = ["any", "all", "dir", "divmod", "enumerate", "eval", "filter", "float", "format", "frozenset", "getattr", "globals", "hasattr", "hash", "help", "hex", "id", "input", "int", "isinstance", "issubclass", "iter", "len", "list", "locals", "map", "max", "min", "next", "object", "oct", "open", "ord", "pow", "print", "property", "range", "repr", "reversed", "round", "set", "setattr", "slice", "sorted", "str", "sum", "tuple", "type", "vars", "zip"]
validString = [string 
               for string in options
               if (len(string) >= 2)
               if (string[0] == 'a')
               if (string[-1] == 'y')
            ]
print(validString)

# Conditional Expressions in List Comprehensions
categories = ["Even" if x %2 == 0 else "Odd" for x in range(10)]
print(categories)

# Let's learn about list comprehensions! You are given three integers x, y & z and representing the dimensions 
# of a cuboid along with an integer n. Print a list of all possible coordinates given by (i, j, k)
# on a 3D grid where the sum of i + j + k is not equal to n. Here, 0 <= i <= x; o <= j <= y; 0 <= k <= z. 
# Please use list comprehensions rather than multiple loops, as a learning exercise.
# Exmpale x = 1 y = 1 z = 2 n = 3 
# Output [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]

x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = [[i, j, k] for i in range (x + 1) for j in range( y + 1) for k in range (z + 1) if i + j + k != n]
print(result)

# 3D List
lst = [[[num for num in range(5)] for _ in range(5)] for _ in range(5)]
print(lst)

# List Comprehension with functions
def square(x):
    return x * x

squared_numbers = [square(x) for x in range(5)]
print(squared_numbers)

# Creating a dictornary
pairs = [('a', 1), ('b', 2), ('c', 3)]
my_dict = {k : v for k, v in pairs}
print(my_dict)

# Set Comprehension
# Remove duplicates from list while applying the function
nums = [1,2,3,4,5,1,2,3]
unique_numbers = {x ** 2 for x in nums}
print(unique_numbers)

# Generator Comprehension
sum_of_squares = sum(x ** 2 for x in range(10))
print(sum_of_squares)