import sys

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                    'C': '-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ' ':' '}

def encrypt(string):
    encrypted = ""
    for x in string:
        if x.islower():
            x = x.upper()
        # print(x)
        if x in MORSE_CODE_DICT:
            encrypted += MORSE_CODE_DICT[x] + ' '
        else:
            print("ERROR")
            exit()
    print(encrypted)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        exit()
    for element in sys.argv[1::]:
        encrypt(element)