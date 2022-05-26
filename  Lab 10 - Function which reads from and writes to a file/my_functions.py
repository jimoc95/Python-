# ScriptName: my_functions.py
# Author: James O'Connor
# Student Number: 113320186

# template for calling functions in another file


from fileinput import filename



def print_function():
    print("I'm in another file :)")

"""
1.  The document tv_shows.txt contains rows of information formatted as dictionaries, each 
dictionary has one key, show_id, and 2 values, which are char_name, and char_address. 
Note: multiple rows for the same show_id, may have different char_name and 
char_address.  A sample of the formatting of the document text is shown. 
{765: "Patrick Star", "stone 1"} 
{765: "Spongebob", "pineapple 1"} 
{825: "Summer Smith", "home address 1"} 
{825: "Rick Sanchez", "space address 1"} 
 
Write a function read_file(input_file) that will read in the content of the input file and return 
a dictionary with show_id as the key and a list of lists as the respective dictionary value for 
each show_id.   
For each show_id key, the char_name, and char_address pair should be combined as a 
separate list within the list of lists.   
Each char_name, and char_address pair should only be added once to the returned 
dictionary (no duplicates values for each show_id key).     
Sample contents of the generated dictionary consists of: 
{765: [["Patrick Star", "stone 1"], ["Spongebob", "pineapple 1"]], 
 825: [["Summer Smith", "home address 1"], ["Rick Sanchez", "space address 1"]]} 

 Items to consider include: 
a. formatting of the original text file. What needs to be removed during formatting. 
b. the text file may contain duplicate information, how will this impact the creation of the 
dictionary keys. 
c. what if characters are in multiple shows. 
d. the order of the dictionaries (and their subsequent values) in the input file should be 
maintained in the returning dictionary (as shown in the example above).
"""


def read_file(input_file: str)-> dict:
    """
    read_file(input_file) -> function that reads in the content of the input file and return a dictionary with show_id as the key 
    and a list of lists as the respective dictionary value for each show_id.
    input_file -> the name of the file ou are reading in -> str
    """
    # Try the below code.
    try:
        # Open the file.
        in_file = open(input_file, "r")        
    
        # initialize the return dictionary
        return_dict = {}

        for line in in_file:
            # Initialize the empty list list_of_lists.
            list_of_lists = []
            # Initialize the empty list values_list.
            value_list = []
            # Strip off the return carriage which is invisible at the end of each line in the file.
            line = line.strip("/n")  
            # Now strip off the leading and trailing white space.
            line = line.strip()
            # Strip off the curly brackets on each end.
            line = line[1:-1]
            # Get the content that is either side of the ":" and put it in a list called content.
            content = line.split(":")
            # The key is the first index in the content list.
            key = content[0].strip()
            # The value is the second index in the content list.
            value = content[1].strip()
            # Add the value to the empty list value_list.
            value_list.append(value)
            # If the key is not in the dictionary add the value list to the list_of_lists and make the list_of_lists the value of the key.
            if key not in return_dict:
                list_of_lists.append(value_list)
                return_dict[key] = list_of_lists
            # Otherwise (i.e. if the key is in the dictionary, add the value of the key to the value for that key already in the dictionary.)
            else:
                return_dict[key].append(value_list)
        # Close the file 
        in_file.close()
        # Return the dictionary
        return return_dict
    # If there is an error return an error message.
    except:
        return "Oops, error..."


"""
2.  Write a function, write_dict(d, output_file), that will write each item in the dictionary, d, 
on a separate line to the document output.txt, in this formatted output: 
id <show_id > <add a tab>has (a character/characters) <char_name> with (an 
address/addresses) of <char_address> 
 
If there are multiple char_name or char_address for a given show_key, these would be 
printed with an " and " between them, as shown below 
id 765  has characters Patrick Starr and Spongebob with addresses of stone 1 and pineapple 
1 
id 825  has characters Summer Smith and Rick Sanchez with addresses of home address 1 
and space address 1 
 
Strengthen all functions in this question by adding exception handling, return "Oops, 
error..." if an error occurs.  Also add hints, docStrings, and comments. 
"""

def write_dict(d: dict, output_file: str) -> None:
    """
    write_dict - function that will write each item in the dictionary, d, on a separate line to the document output.txt
    show_id -> key
    char_name -> first index in the value list
    char_address -> second index in the value list
    """
    # Try the below code....
    try:
        # open the file we are writing to.
        out_file = open(output_file, "w")
        # Initialize the empty return string.
        ret_str = ""
        # for each key, value pair in the dictionary..
        for key, value in d.items():
            # If the value in the dictionary is not a list cast it to a list.
            if type(value) != type(list):
                value = list(value)
            # Initialize the char_name and char_address as empty strings which we will add to and put the key equal to the show_id.
            char_name = ""
            char_address = ""
            show_id = key
            # If there is more than 1 list item (i.e more than one char_name and char_address pair for a show_id).
            if len(value[0][0]) > 1:
                # initialize the counter i
                i=0
                # for each list item in the value of the dictionary (i.e. the char_name and char_address pairs)...
                for index, val in enumerate(value):
                    # The char_name is the first index of the list inside the value list at the index of the counter.
                    char_name = char_name + str(value[i][0]) + " " + "and" + " "
                    # The char_address is the second index of the list inside the value list at the index of the counter.
                    char_address = char_address + str(value[i][1]) + " " + "and" + " "
                    # increment the counter to get the next index values the next time around the for loop.
                    i+=1
                # Define the return string for when there is more than one char_name and char_address pair for a show_id.
                ret_str = ret_str + str(show_id) + " " + "has characters" + " " + str(char_name) + "with addresses of" + " " + str(char_address) + "\n" 
                # Use slicing to remove the last "and" and the return carriage.
                ret_str = ret_str[:-5] + "\n"
            # Otherwise if there is only one char_name, char_address pair...
            else:
                # char_name is the first index of the value in the dictionary.
                char_name = char_name + value[0]
                # char_address is the second index of the value in the dictionary. 
                char_address = char_address + value[1]
                # define the return string
                ret_str = ret_str + str(show_id) + " " + "has a character" + " " + str(char_name) + " " + "with an address of" + " " + str(char_address) + "\n"
        # Write the return string to the file.
        out_file.write(ret_str)
        # Close the file.
        out_file.close()

        return
    # if there is an error return an error message.
    except:
        return "Oops, error..."
    
    