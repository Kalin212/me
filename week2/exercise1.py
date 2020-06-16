"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

#this line defines some_words as a list of strings
some_words = ['what', 'does', 'this', 'line', 'do', '?']

#I think that this will print a variable string that is named (word)
for word in some_words:
    print(word)

#exact same function as above, just the name of the variable is changed
for x in some_words:
    print(x)

#this line will print the list of some_words
print(some_words)

#len tells you how long the list is, and then since it is more than 3 (therefore true), the line 'some_words contains more than 3 words' will be printed
if len(some_words) > 3:
    print('some_words contains more than 3 words')

#gathers information on computer hardware and prints it out
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
