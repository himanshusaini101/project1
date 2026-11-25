# 1. Sorting a tuple of students by their scores in descending order
students = (("Ali", 85), ("ZArham", 92), ("aid", 78), ("Ahmed", 95))
result = tuple(sorted(students, key=lambda x: x[1], reverse=True))
print(result)


# 2. Greeting function with a default message
def greet(name, msg="How do you do?"):
    print(f"hello {name}, {msg}")


# 3. Addition function
def add(x, y):
    result = x + y
    print(f"Result = {result}")


# 4. Demonstrating local variable scope
def my_func():
    x = 10
    print(f"Value inside function: {x}")


# 5. Variadic arguments function to sum multiple numbers
def add2(*num):
    s = 0
    for i in num:
        s = s + i
    print(s)

#6. Tuple names stores persons' names.




def greet(*names):
    for name in names:
        print("Hello", name)
greet("Monica"
      ,"Luke","Steve","John")

# A list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter out only the even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

print(even_numbers)
# Output: [2, 4, 6, 8, 10]
