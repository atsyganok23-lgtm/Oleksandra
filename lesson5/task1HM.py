#Task 1
#Make a program that has some sentence (a string) on input and returns a dict containing all unique words
# as keys and the number of occurrences as values.

sentence = input("Please write your sentence: ")
words = sentence.split()
words_number = {}
for word in words:
    if word in words_number:
        words_number[word] +=1
    else:
        words_number[word] =1
print ("Number of words in your sentence: ")
print (words_number)