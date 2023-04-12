import sys
import string

def error ():
    print("ERROR")
    exit()

if __name__ ==  '__main__':
    if len(sys.argv) != 3:
        error()
    try:
        n = int(sys.argv[2])
    except:
        error()
    arg = ""
    for char in sys.argv[1]:
        if not char in string.punctuation:
            arg+=char
    print([p for p in arg.split() if len(p) > n])
