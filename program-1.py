def convert(number):
    print = " "
if number % 3 == 0:
    print += "Pling"
if number % 5 == 0:
    print += "Plang"
if number % 7 == 0:
    print += "Plong"
if print is " ":
    return str(number)

return print
