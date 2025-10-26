#Extracting numbers.
#Make a list that contains all integers from 1 to 100,
# then find all integers from the list that are divisible by 7 but not a multiple of 5,
# and store them in a separate list. Finally, print the list.
#Constraint: use only while loop for iteration

numbers1 = []
count1 = 0
while count1 <=100:
    numbers1.append(count1)
    count1 += 1

numbers_with_conditions = []
count2 = 0
while count2 < len(numbers1):
    if numbers1[count2] % 7 == 0 and numbers1[count2] % 5 != 0:
        numbers_with_conditions.append(numbers1[count2])
    count2 += 1
print("Numbers divisible by 7 but not by 5:")
print(numbers_with_conditions)
