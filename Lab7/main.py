# ScriptName: main.py
# Author: James O'Connor

# template for calling functions in another file

# import functions from other files - different options
# from functions import print_function
# import functions - when you use this you need to call the function using 'functions.<function_name>'
# this option imports all functions, using '*'
from my_functions import *


def main():
    """
    Call the functions defined in the functions.py file
    """
    #print_function()

    # test count
    #print(count([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1], 4)) #-> 2
    #print(count([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1], 8)) #-> 0
    #print(count("hello", "l")) #-> 2
    #print(count("hello", "h")) #-> 1
    #print(count("hello", "w")) #-> 0
    #print(count(True, 2))#-> error message
    #print(count(1235, 1))#-> error message
    #print(count("p")) #-> 

    #test index
    #print(index("hello", "o")) #-> 4
    #print(index("hello", "p")) #-> -1
    #print(index(True, 2)) #-> Houston we have a problem
    #print(index([4.0, 2.5, 3.7, 5.6, 3.7, 8.3, 10.7], 3.7)) #-> 2
    #print(index([4.0, 2.5, 3.7, 5.6, 3.7, 8.3, 10.7], [3.7])) #-> -1
    #print(index(1234, "oj")) #-> Houston we have a problem
    #print(index("oj")) #-> Houston we have a problem

    #print(get_value("hello", 1)) #-> "e"
    #print(get_value("hello", 2)) #-> "l"
    #print(get_value("hello", 3)) #-> "l"
    #print(get_value("hello", 4)) #-> "o"
    #print(get_value("hello", 0)) #-> "h"
    #print(get_value([1.2, 3.5, 1.2, 9.8, 7.5, 12.8, 1.2], 5)) #-> 12.8
    #print(count(True, 2.5)) #-> "Houston, we have a problem!"
    #print(count(123456, 45))#-> Houston we have a problem
    #print(get_value("hello")) #-> Houston we have a problem

    #print(insert("hello", 1, "a")) #-> "hallo"
    #print(insert("hello", 5, "p")) #-> "hellop"
    #print(insert(True)) #-> Houston, we have a problem
    #print(insert("hello", 26, "phjn")) #-> "hellophjn"
    #print(insert(0, 0, 0)) #-> Houston, we have a problem

    #print(value_in_list("hello", "o")) #-True
    #print(value_in_list("hello", "a")) #-False
    #print(value_in_list([3, 4, 5, 8, 2.7], 2.7)) #-> True
    #print(value_in_list(True, 2)) #-> "Houston, we have a problem!"
    #print(value_in_list(["hello", "yes", "what", "unreal"], "yes")) #-> True
    #print(value_in_list("o")) #-> Houston we have a problem
    #print(value_in_list(True)) #-> Houston we have a problem
    #print(value_in_list(1)) #-> Houston we have a problem

    #print(concat("hello", " world")) #-> "hello world"
    #print(concat([2, 5, 6.5, 57.98, 3.0], [2, 4, 5]))
    #print(concat(True, 2)) #-> "Houston we have a problem!" 
    #print(concat("hello", 2))
    #print(concat(['h', 'a'], [ 'l', 'l', 'o']))
    #print(concat("hello"))

    #print(remove("h", "hello")) #-> "ello"
    #print(remove("l", "hello")) #-> "helo"
    #print(remove("o", "hello")) #-> "hell"
    #print(remove("o", True)) 
    #print(remove("o")) 

    #print(insert("hello", 1, "a")) #-> "hallo"
    #print(insert("hello", 5, "p")) #-> "hellop"
    #print(insert("OUGHTIHERRA", 25, "p"))

if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()
