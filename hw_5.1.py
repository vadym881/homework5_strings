'hw_5.1'
import string
import keyword
variable = input('Name a vaiable: ')
is_valid = (not variable[0].isdigit() and not variable.isupper() and (char not in string.punctuation for char in variable) and variable.count('_') <= 1 and variable not in keyword.kwlist)
print(is_valid)