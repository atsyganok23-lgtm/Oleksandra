#Write a Python program to access a function inside a function
# (Tips: use function, which returns another function)

def function1():
    def function2():
        return "Here is function2 return"
    return function2
func = function1()
print(func())