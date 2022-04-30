# ScriptName: main.py
# Author: James O'Connor
# Student Number: 113320186

# template for calling functions in another file

# import my_functions from other files - different options
# from my_functions import print_function
# import my_functions - when you use this you need to call the function using 'my_functions.<function_name>'
# this option imports all my_functions, using '*'
from my_functions import *


def main():
    """
    Call the functions defined in the functions.py file
    """
    print_function()
    print(to_english(5.5))
    print(to_english())
    print(to_english(-10))
    print(to_english(-100))
    print(to_english(10))
    print(to_english(100))
    print(to_english(900))
    print(to_english(423))
    print(to_english(23))
    print(to_english(3))
    print(to_english(999))
    print(to_english(-999))
    print(to_english("a"))
    print(to_english([]))
    print(to_english(True))
    print(to_english(1000))
    print(to_english(-1000))
    print(to_english(0))
    print(to_english(''))
    print(to_english({}))
    print(to_english(-0))
if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()
