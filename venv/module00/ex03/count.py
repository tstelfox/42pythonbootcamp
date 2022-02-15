import string

def text_analyser(input):
    print("Full length is: ", len(input))
    _upper = 0
    _lower = 0
    _punk = 0
    _space = 0
    for character in input:
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


