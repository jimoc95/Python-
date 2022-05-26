# ScriptName: my_functions.py
# Author: James O'Connor
# Student Number: 113320186

'''
1. create a function called seperated_input() in your‘my_functions.py’file

a.      the function will take four parameters:
i.      param1 -string value
ii.     param2 -string value
iii.    sepr -sep string value(defaults to “”)
iv.     endr -end string value(defaults to “\n”)

b. in your ‘seperated_input()’function, useprint() and its sep and end parameters to modify the output

c. c.check the string inputs for param1 and param2, and capitalize

d. d.You will use the code in the function to modify the  input strings 1 and 2, e.g.
    
    i.seperated_input("phineas","ferb", "and", "rock!!!\n")
        1.printed output -Phineas and Ferb rock!!!

    ii.seperated_input("doofenshmirtz","incorporated", "Evil", "!!!\n")
        1.printed output -Doofenshmirtz Evil Incorporated!!!
'''

def cast_string(param):
    #cast_string - function that takes a parameter, casts it to a string and capitalizes it

    return str(param).capitalize()

def seperated_input(param1, param2, sepr=" ", endr="\n"):
        
        #seperated_input - function to play with print
        #param string_1: string - input string 1
        #param string_2: string - input string 2
        #param sepr: - sep value for print
        #param endr: string - end value for print
        #return:
        
        #take param1, cast to a string and capitalize and store in parameter param1_cap
        param1_cap =  cast_string(param1)

        #take param2, cast to a string and capitalize and store in parameter param2_cap
        param2_cap =  cast_string(param2)


        print(param1_cap, param2_cap, sep=sepr, end=endr)


        return


'''
   2. Ask the user for 3 numbers.  Pass the 3 numbers to a functioncalled three_numbers(number_1, number_2, number_3). If all the numbers are the same returnTrue, otherwise returnFalse.  
      Example of what is returned by the function call is shown(note: ‘->’denotes what is returned from this function):

        a.three_numbers(3, 3, 3) ->True (This is the boolean True and not the string "True")
        b.three_numbers(3, 2, 3)-> False
        c.three_numbers(3,"a", 3)-> False
'''

def three_numbers(num_1, num_2, num_3):
    
    #three_numbers - function determines if 3 numbers inputed have the same value
    #number_1 - integer value
    #number_2 - integer value
    #number_3 - integer value
    
    # if any of the numbers are not integers return False
    if type(num_1) and type(num_2) and type(num_3) != int:
        return False
    
     # if the numbers are equal to eachother return True
    elif (num_1 == num_2 == num_3):
        return True

    # otherwise return False
    else:
        return False
    

'''
3.Write a function called seasons(), that has a parameter called number.  Ask the user for a  number, and pass this number to the function.
  Depending on the number passed to the function, the function will return the corresponding season of the year where 1=Winter, 2=Spring, 3=Summer, and 4 = Autumn. 
  Add code to return an error message if any other number is entered:
    a.seasons(1) -> "Winter"
    b.seasons(5) -> 'Number entered, 5, is outside of input values'
    c.seasons('a') -> 'Input value must be a number'
'''

def seasons(number):
    
    #:seasons - function that determines the corresponding season to the no. entered
    #:number - integer value >0<5
    

    # if the number is not an integer return an error message
    if type(number) != int:
        return "Input value must be a number"

    # if the number is equal to 1 return "Winter"
    elif number == 1:
        return "Winter"

    # if the number is equal to 2 return "Spring"    
    elif number == 2:
        return "Spring" 
    
    # if the number is equal to 3 return "Summer"
    elif number == 3:
        return "Summer"

    # if the number is equal to 4 return "Autumn"
    elif number == 4:
        return "Autumn"

    # Otherwise return error message
    else:
        return "Number entered, " + str(number) + ", is outside of input values"     

    


'''
4. The letter corresponding to a numerical grade percentage is shown below. 
   Ask the user for a  number, and pass this number to a function called grades(), which will return the corresponding grade letter.
   If the user enters a value outside of 0-100 the grade should return ‘X’. 
   If a user enters a non-number, return an error message 'Input value must be a number'

   Numerical Grade  85-100      70-84     55-69     40-54      25-39    0-24
   Letter Grade      “A”         “B”       “C”       “D”        “E”     “F”
'''

def grades(numerical_grade):
    
    #:grades - function that determines the letter grade associated w/ the numerical grade
    #:number - integer value
    

    # if the grade entered is not an integer return an error message
    if type(numerical_grade) != int:
        return "Input value must be a number"

    # else if grade entered between 85 and 100 return "A"
    elif (numerical_grade >=85 and numerical_grade <=100):
        return "A"

    # else if grade entered between 70 and 84 return "B"  
    elif (numerical_grade >=70 and numerical_grade <=84):
        return "B" 

    # else if grade entered between 55 and 69 return "C"    
    elif (numerical_grade >=55 and numerical_grade <=69):
        return "C"
    # else if grade entered between 40 and 54 return "D"   
    elif (numerical_grade >=40 and numerical_grade <=54):
        return "D"

    # else if grade entered between 25 and 39 return "E"    
    elif (numerical_grade >=25 and numerical_grade <=39):
        return "E"

    # else if grade entered between 0 and 24 return "F" 
    elif (numerical_grade >=0 and numerical_grade <=24):
        return "F" 

    # Otherwise return error message      
    else:
        return "Number entered, " + str(numerical_grade) + ", is outside of input values"     

    

'''
  Q5. Ask the user for 2 numbers, and pass these 2 numbers to a function called equal_numbers().
      If the two numbers are equal, then return the square root of the number as a float
     (Use import math at the top of your program to import the math library and use the command math.sqrt()) to get the square root of a number e.g. 
     math sqrt (25.0) gives 5.0). 
     If the two numbers are not equal, then return the squares of both numbers as integers. 
     Recall **for the exponent e.g. 2 ** 3 gives 8:

     a.equal_numbers(25, 25) -> 5.0
     b.equal_numbers(5, 3) -> (25, 9)
     c.equal_numbers('a', 'a') -> 'Input value(s) must be a number'
'''
# import math library
import math

def equal_numbers(num1, num2):
       #equal_numbers - function that checks if two numbers passed are equal and if they are returns the numbers square root
       #num1 - integer value
       #num2 - integer value

    # if num1 and num2 are not integers return error message
    if type(num1 and num2) != int:
        return "Input value(s) must be a number"

    # else if num1 is equal to num2 return the square root of num1 which is equal to num2 
    elif num1 == num2:
        return math.sqrt(num1)

    # Otherwise return the (num1 squared, num2 squared)
    else:
        return (num1 ** 2, num2 ** 2)
   
    


