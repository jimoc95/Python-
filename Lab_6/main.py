# ScriptName: main.py
# Author: James O'Connor
#Student Number: 113320186

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
    #print(seasons(1))
    #print(seasons(2))
    #print(seasons(3))
    #print(seasons(4))
    #print(seasons(20))
    #print(seasons(True))

    
    #print(slice_reverse(12321)) #-> True (This is the boolean True and not the string "True")
    #print(slice_reverse( [1, 2, 3, 2, 1] )) #-> True
    #print(slice_reverse("rotavator")) # True
    #print(slice_reverse(("r","o","t","a","v","a","t","o","r")))
    #print(slice_reverse( " " )) # ->True (a string space)
    #print(slice_reverse("abcdba")) #-> False

    #print(add_to_list(5, [1,3,7,9])) #-> [1,3,5,7,9]
    #print(add_to_list("c", ["a","b","d","e"])) #-> ["a","b","c","d","e"]
    #print(add_to_list(5, [1,5,7,9])) #-> [1,5,7,9]
    #print(add_to_list(5)) #-> [5]
    #print(add_to_list(5, 5)) #-> “Incorrect value defined for param list”
    #print(add_to_list(5, ["a","d","e"])) #- “sort() does not like this mixture of elements”'''

#print(add_to_list_no_sort (5, [1,3,7,9])) #-> [1,3,5,7,9]
#print(add_to_list_no_sort ("c", ["a","b","d","e"])) #-> ["a","b","c","d","e"]
#print(add_to_list_no_sort (5, [1,5,7,9])) #-> [1,5,7,9]
#print(add_to_list_no_sort (5)) #-> [5]
#print(add_to_list_no_sort (5, ["a","b","d","e"])) #-> [5, "a","b","c","d"]
#print(add_to_list_no_sort (5, 5)) #-> “Incorrect value defined for param list”


if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()
