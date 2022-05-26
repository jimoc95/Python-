# ScriptName: my_functions.py
# Author: James O'Connor
#Student Number: 113320186

# template for calling functions in another file

'''
1. 
I want you to rewrite the seasons() function from Lab 4. Within this function, define
a list of the seasons, and select the season based on the input value where 1=Winter,
2=Spring, 3=Summer, and 4=Autumn. Remember list indexing begins at 0. All other
error message handling, param names, etc., in the original function, must be kept.'''



def seasons(number):
    
    #:seasons - function that determines the corresponding season to the no. entered
    #:number - integer value >0<5
    
    #define a list of the seasons
    seasons_list = ['Winter', 'Spring', 'Summer', 'Autumn']
    
    # if the number is not an integer return an error message
    if type(number) != int:
        return "Input value must be a number"

    # if the number is equal to 1 return the first index of the list which is "Winter"
    elif number == 1:
        return seasons_list[0]

    # if the number is equal to 1 return the second index of the list which is "Spring"   
    elif number == 2:
        return seasons_list[1]
    
   # if the number is equal to 1 return the third index of the list which is "Summer"
    elif number == 3:
        return seasons_list[2]

    # if the number is equal to 1 return the fourth index of the list which is "Autumn"
    elif number == 4:
        return seasons_list[3]

    # Otherwise return error message
    else:
        return "Number entered, " + str(number) + ", is outside of input values"     




'''2. This question examines string slicing. Write a function, slice_reverse(input_value),
which determine if the input_value is a palindrome i.e. reads the same backwards as
forwards. The program should return True or False (booleans) depending on the
input. Do not use the Python reverse() function. 
Examples:

slice_reverse(12321) -> True (This is the boolean True and not the string "True")
slice_reverse( [1, 2, 3, 2, 1] ) -> True
slice_reverse( “rotavator” ) -> True
slice_reverse( ("r","o","t","a","v","a","t","o","r”) ) -> True
slice_reverse( “ ” ) ->True (a string space)
slice_reverse( “abcdba” ) -> False'''


def slice_reverse(input_value):

    '''slice_reverse - function which determines if the input value is a palindrome
    '''
    #if input_value is an integer cast it to a string
    if type(input_value) == int:
        input_value = str(input_value)
        
        #if input value stepped in reverse is  = to input value return true otherwise return false 
        if input_value == input_value[::-1]:
            return True
        else:
            return False

    #if input value not an integer just do above step        
    else:
        if input_value == input_value[::-1]:
            return True
        else:
            return False 

'''3. I want you to create a function called add_to_list(value, list), which will return a
sorted list. This function will add value to the list if the list does not already contain
the value. For now, you can assume the list param is already sorted. You can use the
python function “sort()” to sort your returning list. Sort() will not allow you to mix
ints, floats and strings. In your function set an appropriate default value for the list
param. 

Examples:

add_to_list(5, [1,3,7,9]) -> [1,3,5,7,9]
add_to_list("c", ["a","b","d","e"]) -> ["a","b","c","d","e"]
add_to_list(5, [1,5,7,9]) -> [1,5,7,9]
add_to_list(5) -> [5]
add_to_list(5, 5) -> “Incorrect value defined for param list”
add_to_list(5, ["a","d","e"]) -> “sort() does not like this mixture of elements”'''



def add_to_list(value, list=[]):

    '''add_to_list - function that adds a value to a list if the value is not already in the list and returns a sorted list'''
    
    try:
        #if the type of the parameter list is not = to a list return error message
        if type(list) != type([]):
                return "Incorrect value defined for param list"
        #if value parameter not in list add the value onto the end of the list and sort it
        if value not in list:
          
            list.append(value)
            list.sort()
            return list
    # if the value is in the list return the list
        if value in list:
            return list

    except:
        return "sort() does not like this mixture of elements"
        
    
    


'''4. I now want you to create a function called add_to_list_no_sort(value, list), which will
return a sorted list. This function will add value to the list if the list does not already
contain the value. For now, you can assume the list param is already sorted. In your
function set an appropriate default value for the list param. In this function, you
cannot use the python function “sort()” to sort your returning list. But you can now
mix ints, floats and strings. If mixing ints, floats and strings, use ASCII values for
strings when comparing.

You can make 3 assumptions:

1. As we have not covered Loops in great detail, you can assume
the max length of list is 4 elements

2. The input list is already sorted

3. The input list consists of only type of value, i.e., all ints, all
string, etc.

Examples:

add_to_list_no_sort (5, [1,3,7,9]) -> [1,3,5,7,9]
add_to_list_no_sort ("c", ["a","b","d","e"]) -> ["a","b","c","d","e"]
add_to_list_no_sort (5, [1,5,7,9]) -> [1,5,7,9]
add_to_list_no_sort (5) -> [5]
add_to_list_no_sort (5, ["a","b","d","e"]) -> [5, "a","b","c","d"]
add_to_list_no_sort (5, 5) -> “Incorrect value defined for param list”
'''




def add_to_list_no_sort(value, list=[]):
    '''add_to_list_no_sort - returns a sorted list without using the python .sort() function'''

    #if the type of the parameter list is not = to a list return error message
    if type(list) != type([]):
            return "Incorrect value defined for param list"

    #if value parameter not in list add the value onto the end of the list then compare ascii values of the first index with the last and so on to sor the list
    if value not in list:

        list.append(value)
        
        if ord(str(list[4])) < ord(str(list[0])):
                #list = str(list)
                list = list[4], list[0], list[1], list[2], list[3]
                

        elif ord(str(list[4])) < ord(str(list[1])):
                #list = str(list)
                list = list[0], list[4], list[1], list[2], list[3]
                
            
        elif ord(str(list[4])) < ord(str(list[2])):
                #list = str(list)
                list = list[0], list[1], list[4], list[2], list[3]
                

        elif ord(str(list[4])) < ord(str(list[3])):
                list = str(list)
                list = list[0], list[1], list[2], list[4], list[3]
             
    return list 
    
   

           

        
    
   
