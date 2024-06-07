'hw_5.1'
import string
import keyword
is_valid = True
variable_name = input('Еnter the name for a variable: ')
if variable_name[0].isdigit():
    is_valid = False
if variable_name.count('_') > 1 and is_valid:
    is_valid = False
if variable_name in keyword.kwlist and is_valid:
    is_valid = False
if is_valid:
    for char in variable_name:
        if char in string.punctuation and char != '_':
            is_valid = False
            break
if is_valid:
    for char in variable_name:
        if char.isupper():
            is_valid = False
            break

print(is_valid)
