# ScriptName: my_functions.py
# Author: James O'Connor
# Student Number: 113320186

# template for calling functions in another file
# Have to make some of your own assumptions for this one.

from random import choice

def print_function():
    print("I'm in another file :)")


def ships(numShip: int =2) -> list:
    # let's start by randomly selecting 'numShip' space ships
    # numShip should have a default value of 2

    # let's choose from the following 5 ships:
    # Enterprise, Galactica, Rocinante, Serenity and RazorCrest
    '''
        ships - Takes in a number of ships (int) and randomly returns the names of that number of ships.
    '''
    
    try:    # Try below code...
        space_ships = ["Enterprise", "Galactica", "Rocinante", "Serenity", "RazorCrest"]
        ship_list = []              # initialise ship_list as an empty list, this will be the list of ships returned at the end.
        i=0                         # set the counter
        while i < numShip:          # While the counter is less than the number of ships inputed..
            n = choice(space_ships) # n is equal to a random selection from the space_ships list
            if n in ship_list:      # if the randomly selected ship is already in ship_list...
                continue            # Go back to the start of the while loop
            ship_list.append(n)     # add the randomly selected ship to the empty list ship_list 
            i+=1                    # increment the counter
        return ship_list            # Once the loop is complete return ship_list
    except:                         # If there is an error in the above code return an error message
        return "Oops, that does not compute"

def crews(ships: list, crew: list =["captain", "first_mate", "engineer"]) -> str:
    # for each of the 'ships' we need a crew
    # by default, the crew should be composed of a captain, a first_mate
    # and the name of the person who fixes the engines

    # the 'crew' param is a list of the crew to return
    # it must contain one crew title, and a maximum of three crew titles
    
    '''
    assumptions:
    ships -> a list of ships.
    crew - list of crew titles for which a name of the crew member will be returned.
    returns -> list of crew members for a given ship, crew members returned depends on the crew title entered.
    '''
    try:            # Try the following code...

        ships_dict = {"Enterprise": {"captain":"Hook", "first_mate":"George", "engineer":"Mark"},   # Create a dictionary with the ships as keys and the values which are the crew titles are the keys of another dictionary, who's values are the names of the crew members with these titles. 
                "Galactica":{"captain":"Sparrow", "first_mate":"John", "engineer":"Matthew"},       # A dictionary within a dictionary
                "Rocinante":{"captain":"Insano", "first_mate":"Michael", "engineer":"Luke"}, 
                "Serenity":{"captain":"Farrell", "first_mate":"Bob", "engineer":"John"}, 
                "RazorCrest":{"captain": "Kirk", "first_mate":"Jason", "engineer":"Jesus"}}
        currentcrew = []                                    # initialise currentcrew as an empty list which we will use to return our crew members at the end
        for key in ships:                                   # for loop, for the values in the ships list which we will use as keys in our dictionary
            for val in crew:                                # for each crew title in the crew list...
                currentcrew.append(ships_dict[key][val])    # get the value of the key within ships_dict and use that as a key to get the value inside the inner dictionary - name of crew member.
        return currentcrew                                  # append this to the empty list currentcrew and once all keys in ships have been looped over return currentcrew
    
    except:                                                 # If there is an error return the error message
        return "Oops, that does not compute"


def destinations(ships: list) -> list:
    # for each of the 'ships' we need a destination
    # find 3 destinations the ship has been to and randomly return 1 of them
    '''
    ships - list of ships which we will use to look up our dictionary and return they're destinations
    '''
    try:                                # Try the below code

        destination_dict = {"Enterprise": ["Cork", "Mars", "Macroom"], "Galactica": ["Venus", "Cobh", "California"],
            "Rocinante": ["Ballincollig", "Saturn", "Nad"], "Serenity": ["Dromtariffe", "Vancouver", "Planet-X"], 
            "RazorCrest": ["Coolea", "Rylane", "Aghabullogue"]}

        destination = []                # initialise empty list 
        for key in ships:               # loop over ships list
            n = destination_dict[key]   # use list items in ships list as key to look up the dictionary we created
            n = choice(n)               # randomly choose one of the three destinations for each ship 
            destination.append(n)       # append that destination to the empty list
        return destination              # return the list
    except:                             # if there is an error return the error message
        return "Oops, that does not compute"

def recur_func(n:int =5) -> str:
    """
    recursive function to create the countdown string for the countdown function
    n - int - default = 5
    """
    try:

        return_str = ""                 # initialise empty string
        if n == 1:                      # if n is 1 cast it to a str, add it to the empty string and return it
            return_str += str(n)
            return return_str
        else:                           # Otherwise add the number to the string then call the recursive function to do the next number 
            return_str = return_str + str(n) + "," + " " + recur_func(n-1)
        return return_str               # return the str
    except:
        return "Oops, that does not compute"

def countDown(ships:list, my_destinations:list) -> str:
    # each of the ships needs to blast off, so let's count them down
    # for each ship, create a string using the following format
    # 5, 4, 3, 2, 1 - <ship> has blasted off to <destination> using a <loop_type> loop
    #try: 
    """
    function to coundown the blast off of each ship with a seperate string for each
    """
    try:
        overall_cd_str = ""
        for index, ship in enumerate(ships):

            if index+1 % 3 == 1:            # if the mod of the index+1 is 1 i.e first index in every multiple of three 
                cd_str_loop = ""            # initialise empty string
                for val in range(5,0,-1):   # go from 5 to 0 in reverse, adding to the string each time and putting comma and space, then use slicing for last one to remove.
                    cd_str_loop = cd_str_loop + str(val) + "," + " "
                overall_cd_str += cd_str_loop[:-2] + " " + "-" + " " + str(ship) + " has blasted off to " + str(my_destinations[index]) + " using a for loop" + "\n"   
   

            elif index+1 % 3 == 2:          #if the mod of the index+1 is 2 i.e secxond index in every multiple of three
                cd_str_while = ""
                i=5
                while i >= 1:
                    cd_str_while = cd_str_while + str(i) + "," + " "
                    i-=1
                overall_cd_str += cd_str_while[:-2] + " " + "-" + " " + str(ship) + " has blasted off to " + str(my_destinations[index]) + " using a while loop" + "\n"
            

            else:               # Otherwise do the same string as above for every other index using recursion for the countdown loop
                overall_cd_str += recur_func() + " " + "-" + " " + str(ship) + " has blasted off to " + str(my_destinations[index]) + " using recursion" + "\n"
            
        return overall_cd_str   # return the overall string

    except:
        return "Oops, that does not compute"
    

def printout(ships:list, crews:list, destinations:list, format:str) -> str:
    """
    
    """
    # for each ship, create a string composed of the name of the ship,
    # their crew and their destination, in the format:
    # <ship> has a crew of <crew> and is on route to <destination>
    # one ship string per line

    # 'format' should have a default value of "capatalise",
    # but can also take other formats, "lower", "upper", etc
    # Need to use logic to format for different entries, ie. wether there is one, two or three crew members for example.
    crew_str= ""
    dest_str = ""
    ship_str= ""
    print_str = ""

    for index, ship in enumerate(ships):
        crew_str = crews[index] + "," + " "
        dest_str = destinations[index] + "," + " "

        ship_str = ship + " has a crew of " + crew_str[:-2] + " and is on route to " + dest_str[:-2] + "\n"
        print_str = print_str + ship_str

    if format == "capatalise":  
        print_str.capitalize
  

    elif format == "upper":
        print_str.upper
        

    elif format == "lower":
        print_str.lower
        
    return print_str


def toInfinityAndBeyond():
    '''
    '''
    # an example of how I could call the helper functions is shown below

    # variables for ships, crews and destinations
    my_ships = []
    my_crews = []
    my_destinations = []
    my_numShips = 3

    # save 3 ships
    my_ships = ships(my_numShips)

    # save 1 crew members for each ship
    my_crews = crews(my_ships, ["captain"])

    # save 1 destination for each ship
    my_destinations = destinations(my_ships)

    # each of the ships needs to blast off, so lets count them down
    print(countDown(ships, my_destinations))

    # produce a string we can return
    return printout(my_ships, my_crews, my_destinations, "lower")
