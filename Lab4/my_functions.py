# ScriptName: my_functions.py
# Author: James O'Connor
# Student Number: 113320186

# template for calling functions in another file

def print_function():
    print("I'm in another file :)")

'''
Write a Python function to_english(n) that takes a positive or negative integer value 
‘n’ and that returns a string containing the number expressed in English words.

a. For example, if ‘n’ is 142, then the function should return the string “One 
hundred and forty two” (excluding the quotes). Note how the first word is 
capitalized. 

b. Think dictionary for comparison, string concat, division and modulus. 

c. Assume that ‘n’ is a value greater than -1000 and less than 1000 (so between 
-999 and 999).  Any value above or below this range should return the error 
message “Oops”.

d. I will be testing your submission with all edge cases I can think of, so it is 
important to strengthen your code (error message should be “Oops”) and 
add Python hints, docStrings and Comments to your submitted code.

e. Examples: 
i. to_english(142) -> “One hundred and forty two” 
ii. to_english(-142) -> “Minus one hundred and forty two” 
iii. to_english(11) -> “Eleven" 
iv. to_english(42) -> “Forty two" 
v. to_english(9) -> “Nine" 
vi. to_english(999) -> “Nine hundred and ninety nine"
'''

def to_english(n:int=1) -> str:
    '''
    to_english - function that returns a string containing the number n expressed in English words
    n - int
    '''
    try:    # Try the following code

        number_dict = {0:"zero",1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 
                       8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen",
                       14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen",
                       19:"nineteen", 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty",
                       70:"seventy", 80:"eighty", 90:"ninety", 100:"one hundred", 200:"two hundred",
                       300: "three hundred", 400:"four hundred", 500: "five hundred", 600:"six hundred",
                       700:"seven hundred", 800:"eight hundred", 900:"nine hundred"}
        ret_str=""      # initialize the return str
        if type(n) != int or -999 > n > 999 or n == -0:     # raise an error to be handled by try/except if n is not an integer, n is less than -999 or greater than 999 or is -0
            n = n/0                                         # dividing by zero will cause an error which will be caught by try/except

        elif n < 1:                                         # Otherwise if n is negative change it to positive and put "minus" at the start of the return string
                n = n*(-1)
                ret_str = ret_str + "minus" + " "

        tens_and_units = n % 100                            #
        no_of_hundreds = n - tens_and_units                 
        units = tens_and_units % 10
        no_of_tens = tens_and_units - units
        hundreds = n/100
        tens = n/10
        units = n % 10
    
        for key, val in number_dict.items():                # loop over the keys and values in the dictionary number_dict
        
            if n in number_dict:                            # if n is in the number_dict add the value for the key equal to n to the return string
                ret_str = ret_str + number_dict[n]
        
            if hundreds > 1:                                # if there are hundreds in n get the value at the key equal to no_of_hundreds and add it to the return_str - same for the tens and units
                ret_str = ret_str + number_dict[no_of_hundreds] + " "  + "and" + " " + number_dict[no_of_tens] + " " + number_dict[units]
                if units == 0:                              # if the units are zero eg. 20, use slicing to take the last four letters off the string ie. delete "zero" from the end of the string
                    ret_str = ret_str[:-4]
                
            elif hundreds < 1 and tens > 1:                 # If there are no hundreds but there are tens ie. 10 - 99 just get the values for the keys no_of_tens and units and add them to the return string
                ret_str = ret_str + number_dict[no_of_tens]  + " " + number_dict[units]
                if units == 0:                              # if the units are zero eg. 20, use slicing to take the last four letters off the string ie. delete "zero" from the end of the string
                    ret_str = ret_str[:-4]

            elif tens < 1:                                  # if there are no tens just units ie. 1-9 get the value for the key equal to units and add it to the return string
                ret_str = number_dict[units]
            ret_str = ret_str.capitalize()                  # capitalize the first letter of the return string
            return ret_str                                  # return the return string

    except:                                                 # if there is an error return an error message
        return "Oops"


   