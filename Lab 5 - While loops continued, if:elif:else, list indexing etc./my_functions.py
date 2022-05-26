# ScriptName: my_functions.py
# Author: James O'Connor
# Student Number: 113320186

'''2. Write a function, while_loop(max_number), that contains a while loop that loops
from 1 to n, where n is a positive number (passed as parameter - max_number),
saving the number in a list on each loop. The function shall return the list of all
numbers. Example of what is returned by the function call is shown. If no parameter
is passed to the function, while_loop() shall return the list of numbers from 1 to 10:

a. while_loop() -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b. while_loop(5) -> [1, 2, 3, 4, 5] (the list 1 to 5 is returned)

c. Modify the function, while_loop(max_number), so it can also take negative
numbers as input (passed as parameter - max_number). If a negative
number is passed to while_loop(max_number), the list shall return the
numbers from 1 to the negative number:

while_loop(-5) -> [1, 0, -1, -2 ,-3, -4 ,-5]

d. Modify the function, while_loop(max_number), so it will also add the
numbers using an accumulator and add this value as the last value in the list
being returned – note this changes the output from a.) but that is okay
while_loop(5) -> [1, 2, 3, 4, 5, 15]

e. Modify the function, while_loop(max_number), so irrespective of the value of
the max_number parameter, the output list will never go higher than 12, or
lower than -12 (hint: use break):

while_loop(14) -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78]

f. Add error handling – error message for all errors “Did you break the break or
should we continue?” J
'''
def while_loop(max_number=10):
    '''while_loop - loops from 1 to n, where n is a positive number
       max_number - integer'''

    # try the below code
    try: 
        # save_list stores the numbers in an empty list as loop through up to the max_number and will be the list returned at the end 
        save_list = []
        # num_accum is the accumulator and the number at after each loop will be added to it, this will be returned with saved_list once the max_number has been reached
        num_accum = 0
        # if the max_number entered is -0 or a is not of the type int the function will create an error which will then be caught by the try/accept and return "Did you break the break or should we continue?"
        if max_number == -0 or type(max_number) != int: 
            minus_zero = "a"/2
            return minus_zero
        # i is the counter for the following while loops
        i=1
        # if max_number is a positive number execute the following code
        if max_number > 0:
            # while the counter is less than or equal to the max_number entered
            while i <= max_number:
                # add the value at the index i to saved_list
                save_list += [i]
                # add the value i to the accumulator
                num_accum += i
                # increment i for the next loop
                i+=1
                # if i is now greater than 12 break the loop 
                if i > 12:
                    break
            # add the value in the accumulator to the end of saved_list
            save_list.append(num_accum)
            # return saved_list
            return save_list
        # otherwise if max_number entered is a negative number execute the following code
        elif max_number < 0:
            # while i is greater than or equal to the max_number entered
            while i >= max_number:
                # add the value at the index i to saved_list
                save_list += [i]
                # add the value i to the accumulator
                num_accum += i
                # decrement i because we are going in the negative direction as max_number entered was negative
                i-=1
                # if i is less than -12 break the loop
                if i < -12:
                    break
            # add the value in the accumulator to the end of saved_list
            save_list.append(num_accum)
            # return save_list
            return save_list
    # if there is an error in the above code return an error message
    except:
        return "Did you break the break or should we continue?"



'''3. For this question, I want you to develop a function called magic_8_ball(). A Magic 8
Ball is defined as per this very address: https://en.wikipedia.org/wiki/Magic_8-Ball.
“The Magic 8-Ball is a plastic sphere, made to look like an eight-ball, that is used for
seeking advice. It was invented in 1946 by Albert C. Carter and Abe Bookman and is
currently manufactured by Mattel. The user asks a yes–no question to the ball, then
turns it over to reveal an answer in a window on the ball.”
I want you to pass a question using the my_question param of the function and the
function will randomly choose one of the 20 possible answers as provided by the
Wiki (remember to keep your answers exactly as per the website, as I will test for
this text – see image below). Maybe consider using a list to put the replies into. Call
the function using - magic_8_ball(my_question) – this is the default setting for this
function and no matter what extra functionality we add, this should always work.
Figure 1 - the 20 possible answers from the Wiki
Dr. Jason Quinlan Ó UCC 2021 Introduction to Programming
Use this website to learn about random number generation using python3 ()
https://www.w3schools.com/python/ref_random_randint.asp
I now want to see if we can improve our odds of getting a good answer J So, let’s
add a second param, fixed_list, which is a list which contains index values from which
I only want the answer to come from - magic_8_ball(my_question, fixed_list). I am
assuming the answers are read column by column. So, if I pass in a list containing [0,
3, 8] then the function will only return an answer that is randomly chosen from
either “It is certain.” or “Yes definitely.” or “Yes.” Remember: if I call the function
without this parameter, all 20 answers are used to randomly generate the returned
answered.
Oh, and finally for this question, if a -1 is any of the value(s) in the fixed_list, I want
your code to cause an error (any error you want) and return as a string the error that
occurred.
Make sure you add error handling for anything else I could do, as I might try
something silly J I want all non -1 error messages to return “I have spoken.”'''

import random

def magic_8_ball(my_question="", fixed_list=[]):
    '''magic_8_ball - randomly chooses one of 20 possible answers
        my_question - string, the question that you want to ask the magic 8 ball.
        fixed_list - list which contains index values from which I only want the answer to come from'''

    # try the below code
    try:
        # answer_list is a list containing all the possible answers from the magic 8 ball
        answer_list = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful." ]
        # if the value entered for the fixed_list parameter is not of the type list, create an error which will be caught by the try accept and return an error message
        if type(fixed_list) != list: 
            bad_bool = "a"/2
            return bad_bool 
        # if the value entered for the my_question parameter is not of the type string, create an error which will be caught by the try accept and return an error message
        if type(my_question) != str:
            bad_bool = "a"/2
            return bad_bool 
        # if no value is entered for the fixed_list parameter, an empty list has been set as the default value, so if fixed_list is an empty list, (ie. no parameter has been entered for fixed_list) execute the following: 
        if fixed_list == []:
            # i is equal to a random number between 0 and 19
            i =random.randint(0, 19)
            # return the value at the index i - (ie. a random answer from the list of answers for the magic 8 ball)
            return answer_list[i]
        # otherwise if fixed_list is not equal to an empty list (ie. a value has been inputted for fixed_list) execute the following code:
        elif fixed_list != []:
            # for all values in fixed_list
            for v1 in fixed_list:
                # if one of the values is equal to -1, return an error message
                if v1 == -1:
                    return "-1 entered, please enter numbers between 0 and 19"
            # r is a random index number (ie. if there are three values in fixed_list eg. [3, 8, 9] random.randrange() will select a random index number from 0, 1, 2 as an integer not the actual values themselves) selected from fixes_list
            r = random.randrange(len(fixed_list))
            # so now r is an integer which corresponds to a random index number in_fixed list, we now reassign r to be the value in fixed_list at that random index number.
            r = fixed_list[r]
            # then we return the value in answer_list (one of the 20 possible answers from the magic 8 ball) at the index r (the randomly chosen number from fixed_list).
            return answer_list[r]
    # if there is an error in the above code return an error message
    except:
        return "I have spoken."
    

'''4. Create a function called - all_pairs( s1, s2 ) with 2 parameters called:
 s1 - list/string
 s2 - list/string

which creates a list with all pairs of elements from sequences ‘s1’ and ‘s2’,
respectively, note how the second element varies more rapidly than the first
all_pairs( [1,2], "abc" ) -> (False, ["1a", "1b", "1c", "2a", "2b", "2c"])
all_pairs( [], "" ) -> (False, [])
all_pairs( ["abc"], [1,2] ) -> (False, ["abc1", "abc2"])
all_pairs( ["a","b"], "abc" ) -> (False, ["aa", "ab", "ac", "ba", "bb", "bc"])
this all_pairs function returns two values:
the first is a boolean to tell if an exception occurred
the second is output of the function, if no exception occurred,
or [-1] if an exception occurred'''

def all_pairs(s1=[], s2=[]):
    '''all_pairs - creates a list with all pairs of elements from sequences 's1' and 's2'
        s1 - list/string
        s2 - list/string'''

    # try the following code
    try:
        # if only one parameter is given a value create an error and return (True, [-1])
        if s2 == []:
            miss_param = "a"/2
            return miss_param
        # if only one parameter is given a value create an error and return (True, [-1]), but if s1 is an empty list and s2 is an empty string return (False, []) because there was not an exception "" is in s1.
        if s1 == "":
            miss_param = "a"/2
            return miss_param
        # new_list is an empty list which we will add our pairs to once they have been found
        new_list=[]
        # for all values in s1
        for v1 in s1:
            # for all values in s2
            for v2 in s2:
                # cast the values of v1 and v2 to strings so that they can be concatenated, then add them to new_list
                new_list.append(str(v1)+str(v2))
        # once all pairs have been found and added to new_list return the boolean False, indicating that an exception did not occur and the new_list containing the pairs
        return False, new_list
    # if there was an exception return the boolean True, indicating that there was an exception and a list containing the integer -1 
    except:
        return True, [-1]
    

