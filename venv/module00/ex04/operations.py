import sys

def	the_thing():
	if len(sys.argv) > 3:
		print("InputError: too many arguments\n")
	if len(sys.argv) != 3:
		print("Usage: python operations.py <num1> <num2>")
		print("Example:\n\tpython operations/py 10 3")
		return
	num1 = int(sys.argv[1])
	num2 = int(sys.argv[2])
	# int(num1)
	# int(num2)
	print("Sum: ", num1 + num2)
	print("Difference: ", num1 - num2)
	print("Product: ", num1 * num2)
	print("Quotient: ", num1 / num2)
	print("Remainder: ", num1 % num2)

if __name__ == '__main__':
	the_thing()