def divide(dividend, divisor):
    return dividend / divisor

# __name__ is a global variable in python that changes depending on which file you're in
print("mymodule.py:", __name__)

# -- importing from a folder --

import libs.mylib

print("mymodule.py:", __name__)