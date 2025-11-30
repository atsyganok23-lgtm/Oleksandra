#Write a Python program to detect the number of local variables declared in a function.

def local_number(func):
    return func.__code__.co_nlocals

def my_function(a, b):
    result = a + b
    result2 = result * 2
    return result2

print("Local variables in my function:", local_number(my_function))