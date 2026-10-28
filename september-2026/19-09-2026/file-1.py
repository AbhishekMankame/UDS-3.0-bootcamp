a = 2
print(a)
print(type(a))

"""
Type Casting in Python:

Type Casting is the method to convert the Python variable datatype into a certain data type in order to perform the required operations by users.

There can be two types of Type Casting in Python:
- Implicit Type Conversion
- Explicit Type Conversion
"""

user_input_1 = input()
user_input_2 = input()
print("user input 1: ", user_input_1)
print("user input 2: ", user_input_2)

print(type(user_input_1), type(user_input_2))

## Typecasting to `integer`
user_input_1 = int(user_input_1)
user_input_2 = int(user_input_2)

print(type(user_input_1), type(user_input_2))
print(user_input_1 + user_input_2)