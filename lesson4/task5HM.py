#Exclusive common numbers.
#Generate 2 lists with the length of 10 with random integers from 1 to 10,
# and make a third list containing the common integers between the 2 initial lists without any duplicates.
#Constraints: use only while loop and random module to generate numbers

import random
numbers1 = []
count1 = 0

while count1 < 10:
    num = random.randint(1, 10)
    numbers1.append(num)
    count1 += 1

numbers2 = []
count2 = 0

while count2 < 10:
    num = random.randint(1, 10)
    numbers2.append(num)
    count2 += 1

common = []
index = 0
while index < len(numbers1):
    digit = numbers1[index]
    if digit in numbers2 and digit not in common:
        common.append(digit)
    index += 1
print("List 1:", numbers1)
print("List 2:", numbers2)
print("Common:", common)
