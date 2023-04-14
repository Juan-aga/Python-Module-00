import sys

swap = ""

for arg in sys.argv[::-1]:
    if (arg != sys.argv[0]):
        swap += ' ' + arg[::-1]
print (swap[1:].swapcase())
