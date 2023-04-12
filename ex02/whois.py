import sys

if __name__ == '__main__':
    if (len(sys.argv) > 2):
        print("more than one argument are provided")
    elif (sys.argv[1].isalpha() == True):
        print("argument is not an integer")
    else:
        number = int(sys.argv[1])
        if (number == 0):
             print("I'm Zero.")
        elif (number % 2):
            print("I'm Odd.")
        else :
            print("I'm Even")
