#Write a function that takes in two numbers from the user via input(),
# call the numbers a and b, and then returns the value of squared a divided by b,
# construct a try-except block which catches an exception
# if the two values given by the input function were not numbers,
# and if value b was zero (cannot divide by zero).

def my_function ():
    try:
        a = float (input("Enter a number a: "))
        b = float (input("Enter a number b: "))
        result = (a**2)/b
        return result
    except ValueError:
        print("Value entered is not a number.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")

final = my_function()
if final is not None:
    print("The result is", final)
