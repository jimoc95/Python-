# ScriptName: my_functions.py
# Author: James O'Connor
#Student Number: 113320186

# template for calling functions in another file

# Error Checking: Added default values for my_list and value to prevent the function from crashing if only one parameter is inputted
def count(my_list="", value=""):
    '''
    function - count how many times <value> occurs in <my_list>
    :param list: - <my_list> input
    :param value: - <value> to search for
    :return:
    '''
    # try the below code
    try:
        # set counter
        i = 0
        # accumulator to count how many times <value> occurs
        # set to zero to cover no <value> in <list>
        num_values = 0
        # loop over the length of the <list>
        while i < len(my_list):
            # if <value> and <list> index i are the same
            if my_list[i] == value:
                # increment the accumulator
                num_values += 1
            # increment the counter
            i += 1
        # return how many times <value> occurs in <list>
        return num_values
    # if there is an error return an error message
    except:
        return "Houston, we have a problem!"

# Error Checking: Added default values for my_list and value to prevent the function from crashing if only one parameter is inputted
def index(my_list="", value=""):
    '''function to return the first index that value occurs in my_list
        :param list: - <my_list> input
        :param value: - <index>
        :return - index # that value occurs at'''
    # try below code
    try:
        # put counter = 0
        i=0
        # while the counter i is less than the length of my list (ie. pointing to indexes that are in the list)
        while i < len(my_list):
            
            # if the index of i in my list is equal my input value
            if  my_list[i] == value:

            # return the index # of i
                return i
            
            #increment i
            i+=1
        # if the index is not in the list return -1
        return "-1"
    # if there is an error return an error message
    except:
        return "Houston, we have a problem!"

    
# Error Checking: Added default values for my_list and value to prevent the function from crashing if only one parameter is inputted
def get_value(my_list="", index=""):
    '''get_value - function to return the value that occurs in my_list at index
        :param list: - <my_list> input
        :param index: - <index> input
        :return - index # that value occurs at'''
    # try the below code
    try:
        # if the index is less than the length of my_list
        if index < len(my_list):
            #return the value at that index in my_list
            return my_list[index]
        # Otherwise return an error message
        else: return "index input is not in the list"
    # if there is an error in above code return an error message
    except:
        return "Houston, we have a problem!"


# Error Checking: if the value and my_list parameters were different types the function was returning None, added if type(value) == type(my_list): and an else to return an error message if this happens
def remove(value="", my_list=""):
    '''function to return a list with the first occurrence of value removed from my_list
        :param list: - <my_list> input
        :param index: - <value> input
        :return - list'''
    try:
        # if the type of the value parameter is the same as the my_list parameter:
        if type(value) == type(my_list):
            # use the index function created earlier to return the index of param - value in my_list and assign it to parameter removal_index
            removal_index = my_list.index(value)
            # concatonate what comes before removal_index with what comes after removal_index
            return (my_list[:removal_index:1] + my_list[removal_index+1:len(my_list):1])
        # if the type of the value parameter is not the same as the my_list parameter return an error message
        else:
            return "Houston, we have a problem!"
    except:
        "Houston, we have a problem!"

# Error Checking: Added default values for my_list and value to prevent the function from crashing if only one parameter is inputted
def insert(my_list="", index=0, value=""):
    '''insert - function to return my_list,after you have added value at index 
        (remember to check the length of my_listand if index is larger than len(my_list) add as a new index at the end my_list)
        :param list: - <my_list> input
        :param index: - <index> input
        :param value: <value> input
        :return - index # that value occurs at'''
    # try below code
    try: 
        # cast my_list to a list
        my_list = list(my_list)
        # if index is greater than the length of my_list:
        if index > len(my_list)-1:
            # add value to the end of my list
            my_list.append(value)

            # set the counter
            i=0
            # create the empty string str_list
            str_list1 = ""
            # while i is less than the length of my_list
            while i < len(my_list):
                # increment str_list with the value in the index i of my_list
                str_list1 += my_list[i]
                # increment the counter
                i+=1
            # return str_list once i is not less than my_list      
            return str_list1
            
        # else if index is less than the length of my_list:
        elif index < len(my_list):
            # place value in the index of my_list given by the value of index
            my_list[index] = value
            # set the counter
            i=0
            # create the empty string str_list2
            str_list2 = ""
            # while i is less than the length of my_list
            while i < len(my_list):
                # increment str_list2 with the value at the index i in my_list
                str_list2 += my_list[i]
                # increment i
                i+=1
            # return str_list2
            return str_list2
    # if there is an error return an error message
    except:
        return "Houston, we have a problem!"
        

# Error Checking: Added default values for my_list and value to prevent the function from crashing if only one parameter is inputted, also changed code from using "if value in my_list" to the below loop as it was returning True if only one parameter enter
def value_in_list(my_list="", value=""):
    '''value_in_list - function to return True or False if value occurs in my_list
        :param list: - <my_list> input
        :param index: - <value> input
        :return - True/False'''
    # try below code
    try:
        # put counter = 0
        i=0
        # while the counter i is less than the length of my list (ie. pointing to indexes that are in the list)
        while i < len(my_list):
            
            # if the index of i in my list is equal my input value
            if  my_list[i] == value:

            # return the True
                return True
            
            #increment i
            i+=1
        # if the index is not in the list return False
        return False
    # if there is an error return an error message
    except:
        return "Houston, we have a problem!"

# Error Checking: Added default values for my_list and value to prevent the function from crashing if only one parameter is inputted
def concat(list1="", list2=""):
    '''function to return a new list, which is a combination of list1 and list2
        :param list: - <list1>, <list2> input
        :return - combination of list1 and list2 in a new list'''
    # try below code
    try:
        # if the type of list1 or list2 is a string 
        if type(list1) or type(list2) != str:
            # add list1 to list2 and put an empty string between them for a space, put this equal to concat_list
            concat_list = str(list1) + " " + str(list2)
            # return concat_list
            return concat_list
    # if there is an error return an error message
    except:
        return " Houston, we have a problem!"




