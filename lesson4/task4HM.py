#Task 1
#The greatest number
#Write a Python program to get the largest number from a list of random numbers with the length of 10
#Constraints: use only while loop and random module to generate numbers

import random
numbers = []
count = 0

while count < 10:
    num = random.randint(1, 10)
    numbers.append(num)
    count += 1
    max_num = numbers[0]
index = 1

while index < len(numbers):
    if numbers[index] > max_num:
        max_num = numbers[index]
    index += 1

# Print the results
print("All numbers:", numbers)
print("Max number:", max_num)



