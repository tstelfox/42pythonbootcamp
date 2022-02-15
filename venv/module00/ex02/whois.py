import sys

if len(sys.argv) != 2:
    print("ERROR")
    exit()
if (int(sys.argv[1]) % 2) == 0:
    print("I'm zero") if int(sys.argv[1]) == 0 else print("I'm even")
else:
    print("I'm odd")

