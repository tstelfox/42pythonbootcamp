from decimal import Decimal

t = (0, 4, 132.42222, 10000, 12345.67)

string = "module0" + str(t[0]) + ", ex_0" + str(t[1]) + " : " + str(round(t[2], 2)) \
         + ", " + str('%.2E' % Decimal(t[3])) + ", " + str('%.2E' % Decimal(t[4]))

print(string)
