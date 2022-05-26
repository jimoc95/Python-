# ScriptName: my_functions.py
# Author: James O'Connor
# Student Number: 113320186

"""
1. Problem Statement:

Create a takeaway restaurant ordering system which has a menu text file called called menu.txt, this system will take in 
3 parameters from the customer:
i. order_list - list of order codes corresponding to the menu text file indicating which dishes they want to order.
ii. order_quantity - list of quantities corresponding to those items that they want to order
iii. name - the customers name so that we can identify them.

The ordering system will need to be able to calculate a total for the order from the prices listed on the menu txt file 
and display this total to the customer once they have ordered.

The system will also have to create a new file when the first order is placed and add subsequent orders to this file.
Each order added to the file must contain an order number so we can keep track of orders in the kitchen.
This order file must also assign an order to one of the six chefs in the kitchen to make sure the workload is evenly divided.
"""

# template for calling functions in another file

import os.path
from os import path

def takeaway_order(order_list: list[str] = "", order_quantity: list[int] = "", name: str = "Kim Jong-un") -> str:
    '''
    takeaway_order - function which reads in the menu file (menu.txt) and stores each menu item in a dictionary who's key is the item 
                     number and value is a list containing the name of the dish and price. It also writes each order to a 
                     text file called orders.txt and increments the order number each time so that the kitchen can keep track
                     of who's order is who's.
    order_list - list[str] - the item numbers which the customer wants to order
    order_quantity - list[int] - quantities of each item the customer wants to order corresponding to the order_list
    name - str - the customers name
    '''
    # Try the below code....
    try:
        # If the order list or the order_quantity is an empty list return an error message
        if order_list == [] or order_quantity == []:
            return "You must ender an order code and quantity to order!" 
        # If the order list or the order_quantity is not of type list return an error message
        if type(order_list) != list or type(order_quantity) != list:
            return "You must fill in both the order code and order quantity and they must be in the correct format!"
        if type(name) != str:
            return "Your name must be a word!"
        # If the len of the order_list and order_quantity list are not equal return an error message
        if len(order_list) != len(order_quantity):
            return "Quantities do not match items ordered! Please review and order again"
        # open the menu.txt file and store it in the variable in_file
        in_file = open("menu.txt", "r")        
        # initialize the return dictionary
        return_dict = {}
        # Initialize the return string for the customer.
        return_string = ""
        # Go through each line in the menu.txt file...
        for line in in_file:
            # Strip off the return carriage which is invisible at the end of each line in the file.
            line = line.strip("/n")  
            # Now strip off the leading and trailing white space.
            line = line.strip()
             # Get the content that is either side of the ":" and put it in a list called content.
            content = line.split(":")
            # The key for our return dictionary is the first index in the content list.
            key = content[0].strip()
            # The value is the second index in the content list.
            value = content[1].strip()
            # Get the stuff either side of the "," which is the food item and how much it costs and put them in a list
            value = value.split(",")
            # Add this key/value combination to the dictionary
            return_dict[key] = value
        # Set the order total to zero initially
        total = 0
        # Initialize the dish as an empty string
        dish = ""
        # set i = 0 we will use i to access each index in the order_quantity list to get the customers quantity for the item they order
        i = 0
        # loop over the order_list
        for order_no in order_list:
            # if the type of any of the items in the order_list is not a string or is not in the return_dict we created from the menu - return an error message.
            if type(order_no) != str or order_no not in return_dict:
                return str(order_no) + " is not on the menu! Please review your order and try again"
            # order is the value for each order_no in the return_dict i.e. the food items corresponding to the order_no
            order = return_dict[order_no]
            if type(order_quantity[i]) != int:
                return "Order quantity must be a number!"
            # if the quantity at the index of i in the order_quantity is < 1 return an error message 
            elif order_quantity[i] < 1:
                return "Your quantity of " + order_no + ": " + str(order[0]) + " must be greater than or equal to 1"
            # Otherwise if the quantity is > 50 return an error message
            elif order_quantity[i] > 50:
                return "We don't have enough staff to serve this quantity of" + " " + order_no + ": " + str(order[0])
            # add the order_quantity and the food item to the list dish each time, building up an order
            dish = dish + str(order_quantity[i]) + "x " + order[0].strip() + "," + " "
            # calculate the total for the order by adding the order_quantity multiplied by the price of the food item each time.
            total = total + (order_quantity[i] * float(order[1].strip()))
            # Increment i to get to the next index in the order_quantity list. 
            i+=1
        # Create a return string confirming the customer's order details with a total for the order
        return_string = "Thanks " + name + "! " + "Your order of " + dish[:-2] + " has been confirmed, your total today is " + "€" + str(total) 
        # Close the menu.txt file
        in_file.close()
        # Initialize order_number as 1
        order_number = 1
        # Initialize chef_number as 1
        chef_number = 1
        # If a file called orders.txt exists in the directory i.e. if there has already been an order...
        if path.exists("orders.txt") == True:
            # open the orders.txt file
            order_file = open("orders.txt", "r")
            # store the last line (i.e. latest order) in the variable last_order_line 
            last_order_line = order_file.readlines()[-1]
            # Get the order # of the last line, cast to an int and store it in order_number
            order_number = int(last_order_line[18])
            # Increment order_number  
            order_number += 1
            # Get the Chef No from the last line and store it in the variable chef_number
            chef_number = int(last_order_line[9])
            # if chef_number is < 6 increment chef_number
            if chef_number < 6:
                chef_number += 1
            # Once chef_number is 6 set it back to 1 - we only have 6 chefs
            else:
                chef_number = 1
        # Create an order_str which we will write to the orders.txt file
        order_str = "Chef No: " + str(chef_number) + "," + " Order " + str(order_number) + ": " + dish[:-2] + " " + "- " +  "Total" + " " + "€" +str(total) + "\n" 
        # Open the orders.txt file - and we are going to append to the file - add the order to the file
        out_file = open("orders.txt", "a")
        # Write the order_str to the file
        out_file.write(order_str)
        # Close the file
        out_file.close()
        # Return the return string with the customers order confirmation
        return return_string
    # If there is an error in the above code return an error message
    except:
        return "Oops..."