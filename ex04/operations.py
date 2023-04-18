import sys

def operations (num1, num2):
    num1 = int(num1)
    num2 = int(num2)
   
    print("Sum:        %i"%(num1 + num2))
    print("Difference: %i"%(num1 - num2))
    print("Product:    %i"%(num1 * num2))
    try:
        num1 / num2
    except ZeroDivisionError:
        print("Quotient:   ERROR (division by zero)")
        print("Remainder:  ERROR (modulo by zero")
    else:
        print("Quotient:   %f"%(num1 / num2))
        print("Remainder:  %i"%(num1 % num2))

if __name__=='__main__':
	if len(sys.argv) < 3:
		print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
	elif len(sys.argv) > 3:
		print("too many arguments")
	else:
		try:
			operations(int(sys.argv[1]), int(sys.argv[2]))
		except:
			print("only integers")
#	elif sys.argv[1].isnumeric() and sys.argv[2].isnumeric():
#        operations(sys.argv[1], sys.argv[2])
#    else:
#        print("only integers")
