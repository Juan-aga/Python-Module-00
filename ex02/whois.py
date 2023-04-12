import sys

if __name__ == '__main__':
   if len(sys.argv) > 2:
        print("more than one argument are provided")
        exit()
   elif len(sys.argv) == 1:
       exit()
   try:
       number = int(sys.argv[1])
   except ValueError:
       print("argument is not an integer")
   else:
       if (number == 0):
            print("I'm Zero.")
       elif (number % 2):
           print("I'm Odd.")
       else :
           print("I'm Even")
