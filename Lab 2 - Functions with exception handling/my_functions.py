# ScriptName: my_functions.py
# Author: James O'Connor
# Student Number: 113320186

'''2. I want you to rewrite the fizz_buzz() function from item 1. In the original function, a
    number was passed to the function. For multiples of 3 the function returned “Fizz”.
    For multiples of 5, returned “Buzz”. For numbers which are multiples of both 3 and 5
    returned “FizzBuzz”. I want this functionality to remain in the new function
    (remember default values).
    I now want you to add two additional parameters, namely divisor_1 (parameter 2)
    and divisor_2 (parameter 3). Now the function requirements are: For multiples of
    divisor_1 the function return “Fizz”. For multiples of divisor_2, return “Buzz”. For
    numbers which are multiples of both divisor_1 and divisor_2 return “FizzBuzz”.
    Examples of what is returned by the function call are shown:

        a. fizz_buzz(3) -> 'Fizz'
        b. fizz_buzz(5) -> 'Buzz'
        c. fizz_buzz(15) -> 'FizzBuzz'
        d. fizz_buzz(14) -> 14
        e. fizz_buzz('a') -> 'Input value(s) must be a number'
        f. fizz_buzz(4, 4, 6) -> "Fizz"
        g. fizz_buzz(6, 4, 6) -> "Buzz"
        h. fizz_buzz(15, 3, 5) -> "FizzBuzz"
'''

def fizz_buzz(num1, divisor_1=3, divisor_2=5):
    '''function which returns 'fizz' if num1 is a multiple of 3, 
       returns 'buzz' if num1 is a multiple of 5, 
       returns 'FizzBuzz' for numbers which are multiples of both'''
    # try to run below code   
    try: 
        # if num1, divisor_1 or divisor_2 are integers do the following
        if type(num1 and divisor_1 and divisor_2) == int:
            # if num1 is a multiple of 3 and 5, return 'FizzBuzz'
            if (num1%divisor_1 ) == 0 and (num1%divisor_2) == 0:
                return 'FizzBuzz'
            # if num1 is divisible by 3, return 'Fizz'
            elif (num1%divisor_1) == 0:
                return 'Fizz'
            # if num1 is divisible by 5 return 'Buzz'
            elif (num1%divisor_2) == 0:
                return 'Buzz'
            # Otherwise return num1
            elif type(num1 or divisor_1 or divisor_2) == bool:
                return("Input value(s) must be a number") 
            else:
                return num1
    #If above code breaks return error message
    except:
        return("Input value(s) must be a number") 

# Error Checking: fizz_buzz would return the name of the Boolean when passed, so added elif to return an error message when a boolean is passed

'''
Q3. I want you to rewrite the grades() function from Lab 4, adding a parameter called number. In the original function, you passed a number to the function, which would return the corresponding Letter Grade. The function will now also take a Letter Grade and should return the Numerical Grade range. Examples of what is returned by the function call are shown:

grades(86) -> "A" (the string A is returned)
grades("A") -> "85-100" (the string 85-100 is returned)
grades(110) -> "The input numerical grade is outside the range supported"
grades("H") -> "The input letter grade is outside the range supported" Update error message handling in the new function to handle the different inputs (if
not str or int) – 'Input value must be a number or a letter'.'''


def grades(number):
    '''grades - function that determines the letter grade associated w/ the numerical grade
    numerical_grade - integer value
    number - string value'''
    
    # if number is an integer check which grade range the number is within and return its corresponding letter grade.
    if type(number)==int or type(number) == float:

        # else if grade entered between 85 and 100 return "A"   
        if(number >=85 and number <=100):
            return "A"

        #if grade entered between 70 and 84 return "B" 
         
        if (number >=70 and number <=84):
            return "B" 

        #if grade entered between 55 and 69 return "C"    
        if (number >=55 and number <=69):
            return "C"

        #if grade entered between 40 and 54 return "D"   
        if (number >=40 and number <=54):
            return "D"

        #else if grade entered between 25 and 39 return "E"    
        if (number >=25 and number <=39):
            return "E"

        #else if grade entered between 0 and 24 return "F" 
        if(number >=0 and number <=24):
            return "F" 

        # If the number inputted which is an integer is not between any of these ranges, return error message. 
        else: 
            return "The input numerical grade is outside the range supported"

    # Check if it is a string.
    elif type(number)==str:

        # If the string is = "A" return "85-100"
        if number == "A":
            return "85-100"

        # If the string is = "B" return "70-84"
        if number == "B":
            return "70-84"

        # If the string is = "C" return "55-69"
        if number == "C":
            return "55-69"

        # If the string is = "D" return "40-54"
        if number == "D":
            return "40-54"

        # If the string is = "E" return "25-39"
        if number == "E":
            return "25-39"

        # If the string is = "F" return "0-24"
        if number == "F":
            return "0-24"

        # Otherwise return error message      
        else:
                return "The input letter grade is outside the range supported"
    # Otherwise return an error message
    else:
        return("Input value must be a number or a letter")        
            
#Error Checking: grades would not take a float, added this functionality to the first if statement
