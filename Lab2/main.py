# ScriptName: main.py
# Author: <add your name here>

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

    print(times_tables(5, 12))
    print(getSet([1,1,2,3,3,4,5,5,5,6])) # -> 2,4,6
    print(all_even([1,2,3,4]))
    print(all_even([3,1,3,4]))
    print(all_even([3,75,7]))
    print(checkAllEven([2,4,6,8,10,12]))
    print(checkAllEven([2,4,3,6,8]))
    print(in_order(1, 5, 7))
    print(in_order(25, 5, 7))
    print(in_order(3, 75, 7))
    print(create_diction([1,1,2,1,3,4,5,6,4,7], ["a","b","c","d","e","f","g"]))
    print(create_diction([1,2,3,4,2,3,4], [10, 20, 30, 40, 21, 31, 41] ))
if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()
