def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculate(fun, a, b):
    return fun(a, b)

print(calculate(add, 10, 5))
print(calculate(subtract, 10, 5))
print(calculate(multiply, 10, 5))
print(calculate(divide, 10, 5))