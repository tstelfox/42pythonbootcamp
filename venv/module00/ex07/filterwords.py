import sys
import string

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("AO")
        exit()
    thing = sys.argv[1]
    num = int(sys.argv[2])
    print(thing)
    comprehend = [x.translate(str.maketrans('', '', string.punctuation)) for x in thing.split() if len(x) > num]
    print(comprehend)