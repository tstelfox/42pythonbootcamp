import string
import sys

def text_analyser(stuff=None, nope=None):
    if nope:
        print("ERROR")
        return
    if stuff is None:
        print("Enter some shit")
        print(">>> ", end="")
        # stuff = sys.stdin.readline()
        stuff = input()
    print("Full length is: ", len(stuff))
    _upper = 0
    _lower = 0
    _punk = 0
    _space = 0
    for character in stuff:
        if character.isupper():
            _upper += 1
        elif character.islower():
            _lower += 1
        elif character in string.punctuation:
            _punk += 1
        elif character.isspace():
            _space += 1
    print("- ", _upper, " upper letters")
    print("- ", _lower, " lower letters")
    print("- ", _punk, " punctuation marks")
    print("- ", _space, " spaces")


