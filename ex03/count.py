import string
import sys


def text_analyzer(text=""):
    """\n\tThis function counts the number of upper characters, lower characters,\n\tpunctuation and spaces in a given text."""
    if (text == ""):
        while 42:
            try:
                text_analyzer(input("What is the text to analyze?\n>> "))
            except:
               return
            else:
               return
    if (not isinstance(text, str)):
         print("argument is not a string")
         return
    upper = 0
    lower = 0
    space = 0
    punct = 0
    compare = string.punctuation
    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char == ' ':
            space += 1
        elif compare.find(char) > -1:
            punct += 1
    print("The text contains %i character(s):"%len(text))
    print("- %i upper letter(s)"%upper)
    print("- %i lower letter(s)"%lower)
    print("- %i punctuation mark(s)"%punct)
    print("- %i space(s)"%space)

if __name__=='__main__':
    if len(sys.argv) > 2:
        print("Error")
        quit
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        text_analyzer()
