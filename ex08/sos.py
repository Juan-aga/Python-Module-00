import sys

morse = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....',
        'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 
        'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
        'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..',
        '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....',
        '7':'--...', '8':'---..', '9':'----.', '0':'-----', " ":"/"}

def error ():
    print("ERROR")
    exit()

if  __name__ == "__main__":
    mes = ""
    for i in range(1, len(sys.argv), 1):
        if " " in sys.argv[i]:
            for c in sys.argv[i].split():
                mes += c + " "
        else:
            mes += sys.argv[i] + " "
    for word in mes.split():
       if not word.isalnum():
            error()
    encoded = ""
    for char in mes:
        encoded += (morse[char.upper()] + " ")    
    if encoded != "":
    	print(encoded[:-2])
