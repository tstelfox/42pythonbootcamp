import sys

def print_opposite(letter):
    if letter.isupper():
        return letter.lower()
    elif letter.islower():
        return letter.upper()
    else:
        return letter

thing = []
first = True
for arg in sys.argv:
    if first:
        first = False
    else:
        thing.append(arg.split()[::-1])
thing = thing[::-1]
yeet = 0
to_print = ""
for word in thing:
    for subunit in word:
        single_word = ""
        yeet += 1
        for letter in subunit[::-1]:
            single_word += print_opposite(letter)
        to_print += single_word + " "
to_print = to_print[:-1]
print(to_print)
