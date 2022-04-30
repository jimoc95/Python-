# ScriptName: my_functions.py
# Author: James O'Connor
# Student Number: 113320186

'''
    1. Write a function - times_tables(num1, num2) - that prints the times tables for two 
numbers passed as parameters. For example, for a call of times_tables(5, 12) the 
program should return a string that can be printed with the following format: 
    5 x 1 = 5 
    5 x 2 = 10 
    ... these three dots represent the other “5 x N” tables, make sure you provide tables 
   5 x 12 = 60 
Strengthen your code (error message should be “Oops”) and add Python hints, 
docStrings and Comments to your submitted code. 5 marks. 
    
'''


from xmlrpc.client import boolean


def times_tables(num1: int, num2: int)-> str:
    """
    function that prints the times tables for two numbers passed as parameters
    num1 - int
    num2 - int
    returns - string of times tables each on their own line.
    """
    i=1
    empty = ""
    while i <= num2:        # While i is less than num2 
        product = num1*i    # create a variable for num1 multiplied by the value of i ie. the times part of the times tables
        calc = str(num1)+ " " + "x" + " " + str(i) + " " + "=" + " " + str(product) + "\n"  # Create a variable for the calculation putting a return carriage at the end so that each one goes on a new line.
        empty+=calc         # Add the calculation to the empty string each time it goes around the while loop
        i+=1                # Increment the counter
    return empty            # return the empty string that the times tables have been added to.

'''
2. Write a function called getSet( ) that takes a list, inputList, as a parameter. The 
function should return a new list that contains the unique values in inputList. You 
should use while loops for any iteration. 
Strengthen your code (error message should be “Oops”) and add Python hints, 
docStrings and Comments to your submitted code.  8 marks. 

'''
def getSet(inputList: list)-> list:
    """
    Function that returns a new list that returns the unique values in inputList
    inputList - list
    returns - list
    """
    try:                                        # Try the following code:
        i = 0                                   # Set counter at 0
        new_list = []                           # Create an empty list which we will add the unique values to
        while i < len(inputList):               # While the counter i is less than the length of the inputList...
            if inputList[i] not in new_list:    # If the value at the index i of the inputList is not in the empty list, add that value to the empty list
                new_list.append(inputList[i])
            i+=1                                # Increment the counter
        return new_list                         # Return the previously empty list, new_list once all of the values in inputList have been checked
    except:                                     # If there is an error in the above code, return an error message.
        return "Oops"  

'''
    3. Write a function - all_even( a_list ) -  that returns a Boolean True if a list of numbers, 
passed as a parameter, is in ascending order. For example, [1,2,3,4] would return 
True while [2,1,3,4] would return False. 
Strengthen your code (error message should be “Oops”) and add Python hints, 
docStrings and Comments to your submitted code.  7 marks. 

'''
def all_even(a_list: list)-> bool:
    """
    Function that returns Boolean True if a list of numbers is in ascending order
    a_list - list
    returns - Boolean - True if numbers in ascending order and False if not
    """
    try:                                    # Try the following code:
        i=1                                 # Set the counter to 1, the loop will begin on the second value in the list
        while i < len(a_list):              # Set up a loop while i is less than the length of the list a_list
            if a_list[i] < a_list[i-1]:     # if the value at the index i in a_list is smaller than the previous value ie. Not ascending - return the Boolean False
                return False
            i+=1                            # Increment the counter
        return True                         # If the if statement is False - numbers in ascending order - return True 
            
    except:                                 # If there is an error return an error message
        return "Oops"

'''
4. Write a function – checkAllEven( lst ) - that returns a Boolean True if a list of numbers 
(passed as a parameter) are all even, otherwise the function should return False. 
Strengthen your code (error message should be “Oops”) and add Python hints, 
docStrings and Comments to your submitted code.  8 marks. 

'''
def checkAllEven(lst: list)-> bool:
    """
    Function that returns a Boolean True if a list of numbers are all even, otherwise it returns False.
    lst - list
    return - Boolean - True if even, False if odd
    """
    try:                        # Try the below code:
        for val in lst:         # For the values in the list "lst"...
            if val % 2 != 0:    # If when divided by 2 the values return a modulus that is not zero ie. they are odd - return the Boolean False
                return False
        return True             # If the above if statement is False - they are even - return the Boolean True
    except:                     # If there is an error return an error statement
        return "Oops"


'''
5. Write a function – in_order( ) - that takes three integers, a, b and c, as parameters. 
Your program should return a message to the user, “all numbers in order”, indicating 
if the number are in ascending order and if not, the message should be “not in 
order”. 
Strengthen your code (error message should be “Oops”) and add Python hints, 
docStrings and Comments to your submitted code.  5 marks. 
 
'''
def in_order(a: int,b: int ,c: int)->str:
    """
    Function that returns “all numbers in order” if the number are in ascending order and if not, the message should be “not in 
    order”
    a, b, c - int
    return - str - "all numbers in order" if numbers a,b and c are in ascending order and "not in order" if not 
    """
    try:                                    # Try the below code:
        a_list = [a, b, c]                  # Create a list which contains the values for a, b and c
        i=1                                 # Set the counter to 1, the loop will begin on the second value in the list
        while i < len(a_list):              # Set up a loop while i is less than the length of the list a_list
            if a_list[i] < a_list[i-1]:     # if the value at the index i in a_list is smaller than the previous value ie. Not ascending - return "not in order"
                return "not in order"
            i+=1                            # Increment the counter
        return "all numbers in order"       # If the if statement is False - numbers in ascending order - return "all numbers in order"
    except:                                 # If there is an error in the above code return error message.
        return "Oops"



'''
6. Write a function – create_diction( list_of_keys, list_of_values ) – which takes two 
lists, one of keys and one of values and returns a dictionary.  The i index of 
list_of_keys matches to the i index of list_of_values.   Keys can repeat, if this occurs, 
the values should be added as a list of values. Example: 
list_of_keys = [1,2,3,4,2,3,4] 
list_of_values = [10, 20, 30, 40, 21, 31, 41] 
returned dictionary -> {1: 10, 2: [20, 21], 3: [30, 31], 4: [40, 41]} 
Strengthen your code (error message should be “Oops”) and add Python hints, 
docStrings and Comments to your submitted code.   Not an exam question 

'''
def create_diction(list_of_keys: list, list_of_values: list)-> dict:
    """
    Function which takes two lists, one of keys and one of values and returns a dictionary.
    list_of_keys - list
    list_of_values - list
    return - dict where the keys are the values from list_of_keys and the values are the values from list_of_values
    """
    try:                                                    # Try the following code:
        i=0                                                 # Set the counter
        new_dict = {}                                       # Create an empty dictionary
        while i < len(list_of_keys):                        # Create while loop to go over the length of the list, list_of_keys
            new_dict[list_of_keys[i]] = list_of_values[i]   # Add the values at the index i in both list_of_keys and list_of_values to the empty dictionary as keys and values
            i+=1                                            # Increment the counter
        return new_dict                                     # Return the created dictionary "new_dict"
    except:                                                 # If there is an error return an error message
        return "Oops"