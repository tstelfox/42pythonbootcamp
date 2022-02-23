t = (0o2, 0o2, 2022, 22, 22)

string = ""
for i in range(3):
    string += str(t[i])
    if i != 2:
        string += '/'

string += " " + str(t[3]) + ":" + str(t[4])
print(string)