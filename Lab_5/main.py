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
    Call the functions defined in the my_functions.py file
    """
    
    #print(grades(25.3)) #"A" (the string A is returned)
    #print(grades("A")) #"85-100" (the string 85-100 is returned)
    #print(grades(110)) #"The input numerical grade is outside the range supported"
    #print(grades("H")) #"The input letter grade is outside the range supported" 
    #print(grades(True))#Update error message handling in the new function to handle the different inputs (if not str or int) #'Input value must be a number or a letter'.
    #print(grades(*))

    print(fizz_buzz(True)) #-> 'Fizz'
    print(fizz_buzz(5)) #-> 'Buzz'
    print(fizz_buzz(15)) #-> 'FizzBuzz'
    print(fizz_buzz(14)) #-> 14
    print(fizz_buzz("a")) #-> 'Input value(s) must be a number'
    print(fizz_buzz(4, 4, 6)) #-> "Fizz"
    print(fizz_buzz(6, 4, 6)) #-> "Buzz"
    print(fizz_buzz(15, 3, 5)) #-> "'FizzBuzz'"
    print(fizz_buzz("f"))
    print(fizz_buzz(0))

if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()
