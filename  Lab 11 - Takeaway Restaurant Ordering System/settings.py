# ScriptName: settings.py
# Author: James O'Connor
# Student Number: 113320186

# settings for your tests

# ===================================================
# functions to call
test_func = ["takeaway_order", # print_function example
            ]

# ===================================================
# input parameter(s) and values to pass to the functions
param_name = [
              # print_function example
              ["order_list"], ["order_quantity"], ["name"]

              # your function parameter name(s) - list of String list(s) - with one name per parameter
              # [""],
             ]

input_vals = [
              
              [ [["I12", "I6", "I15", "I10", "I24"], [1, 3, 2, 5, 1]], [["I22", "I3"], [1, 3, 2]], [["I22", "I3"], [1]], [["I15", "I4", "I13"], [1, 5, 7], "Jimmy"],
                [["a", "I4", "I13"], [1, 5, 7], "Jimmy"], [["I21", "I4", "I13"], ["a", 5, 7]], [["I21", "I4", "I13"], [-10, 5, 7]], [["I14", "I4", "I13"], [51, 5, 7]], 
                [["I14", "I4", "I13"], [1, 5, 7], 7], [True, 7], [7], [[], []], [], [True, 7, float], [["I2", "I17", "I14", "I13", "I22", "I9"], [1, 3, 2, 5, 1, 18], "Bob"]
              ]
              
             ]

# ===================================================
# output values I must test against for this function
outputlist = [
              # print_function example
              [ "Thanks Kim Jong-un! Your order of 1x Spaghetti Bolognese, 3x Burrito, 2x Garlic Bread, 5x Butter, 1x Mineral Sparkling Water has been confirmed, your total today is €77.42", 
                "Quantities do not match items ordered! Please review and order again", "Quantities do not match items ordered! Please review and order again", "Thanks Jimmy! Your order of 1x Garlic Bread, 5x Mixed Olives, 7x Tacos has been confirmed, your total today is €112.93",
                "a is not on the menu! Please review your order and try again", "Order quantity must be a number!", "Your quantity of I21: Espresso must be greater than or equal to 1",
                "We don't have enough staff to serve this quantity of I14: Lasagna", "Your name must be a word!", "You must fill in both the order code and order quantity and they must be in the correct format!"
                "You must fill in both the order code and order quantity and they must be in the correct format!", "You must ender an order code and quantity to order!", "You must fill in both the order code and order quantity and they must be in the correct format!"
                "You must fill in both the order code and order quantity and they must be in the correct format!", "Thanks Bob! Your order of 1x Stew, 3x Gelato, 2x Lasagna, 5x Tacos, 1x Cappuccino, 18x Shepard's Pie has been confirmed, your total today is €459.0"
              ],
              
              # your function return values to be tested against
              # [ , , , , , , 
              # ],
             ]
