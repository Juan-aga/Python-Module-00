kata = (19,42,21)

to_print = "The {size} numbers are: ".format(size = len(kata))
for number in kata:
    to_print += str(number) + ", "
print(to_print[:-2])
