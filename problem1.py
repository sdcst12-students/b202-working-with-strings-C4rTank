"""
String handling is important.  We can break a string into pieces to help us look at parts one at a time using the string.split function.
Have the user enter a sentence or paragraph and gives a word count.
"""

SENTENCE = input("Enter a sentence : ")

WORD_COUNT = len(SENTENCE.split())

#There is one word
if WORD_COUNT == 1:
    print("There is",WORD_COUNT,"word in the sentence")
#There are more words
else:
    print("There are",WORD_COUNT,"words in the sentence")

#DONE