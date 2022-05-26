# ScriptName: my_functions.py
# Author: James O'Connor
# Student Number: 113320186

# template for calling functions in another file



def print_function():
    print("I'm in another file :)")


'''
1. Rewrite this function using 'while' loops instead of 'for' loops. Strengthen your code   
(error message should be “Oops”) and add Python hints, docStrings and Comments to
your submitted code.
def F(s1, s2):
r = []
for e1 in s1:
for e2 in s2:
if e1 == e2:
 r += [e1]
 break
return r
(Recall that break terminates only the innermost enclosing loop).
'''
# When doing these questions copy the original code and make sure they both work then start changing it to the while loop.
# When testing the code, test them side by side, pass in the same parameters so you will see straight away it is wrong.

def F(s1: string, s2: string):  # We need two for loops if we have two loops coming in and we want to go over both to dee what is similar etc.
    '''
    F creates a list of the items which are common to both s1 and s2
    s1 & s2 - string
    '''
    r = []
    for e1 in s1:
        for e2 in s2:
            if e1 == e2:
                r += [e1]       # If you want to add something to a list it needs to be a list, this is why we need to define e1 as a list, we could also cas to a list using list(e1)
                #r.append(e1)   # This will append something to an existing list
                break
    return r 

def FW(s1: list, s2: list)-> list:      # When changing for to a while loop try not to chnage the magic inside the first for loop if at all possible.
    '''
    F creates a list of the items which are common to both s1 and s2
    s1 & s2 - lists
    '''
    try:
        i=0
        r=[]
        while i < len(s1):      # define inner while loop and make sure it is tabbed in, then define an outer while loop and make sure its tabbed in
            e1 = s1[i] 
            j=0                 # You need to reset j to zero everytime you come into your inner loop, so do not define j outside the first loop.
            while j < len(s2):
                e2 = s2[j]
                if e1==e2:
                    r += [e1]
                    break
                j+=1                # Counter needs to be within your loop otherwise nothing is counted and you get a forever loop
            i+=1
        return r 
    except:
        return "Oops"
'''
2. Write an iterative function iter_factorial( n ) that calculates and returns the factorial, as
an integer, of a given number n. Recall that factorial of 5 (5!) is 5 * 4 * 3 * 2 * 1 = 120
Strengthen your code (error message should be “Oops”) and add Python hints,
docStrings and Comments to your submitted code.

'''
# You have to decide what your function is going to do ie. state your assumptions
# assumptions, neg numbers, zero, positive numbers
def iter_factorial(n: int) -> int:
    '''
    Calculates and returns the factorial of a given number n as an integer
    n - integer
    assumptions: negative numbers and zero return 1
    '''
    try:
        ret_val=1

        for val in range(n):
            print(val+1)
            ret_val *= val+1

        return ret_val

    except:
        return "Oops"

    # try:
    #     i=0
    #     factorial_digit = 0
    #     while i <= n:
    #         calc = n*i
    #         factorial_digit 
    #         i+=1
        
    #     return factorial_digit
    # except:
    #     return "Oops"

    
'''
3. The function below accepts a string as an input and returns a string with the vowels
removed. Rewrite this function using a while loop. Strengthen your code (error message
should be “Oops”) and add Python hints, docStrings and Comments to your submitted
code.

def removeVowels(sentence):
vowels = “aeiou”
filtered_list = []
for l in sentence:
if l not in vowels:
 filtered_list.append(l)
return “”.join (filtered_list)

'''
def removeVowels(sentence: str)-> str:
    vowels = "aeiou"
    filtered_list = []
    l=0
    while l < len(sentence):
        if sentence[l] not in vowels:
            filtered_list.append(sentence[l])
            #print(sentence[l])
    l+=1
    return filtered_list



'''
4. Write an iterative function hailstone( n ) that generates the hailstone sequence of a
given positive number n and returns the sequence as a list. The ‘hailstone’ sequence
starts with a positive integer and defines the next number in the sequence as follows: if
n is even, the next value is n/2. If n is odd, the next value is 3n + 1. The sequence will
converge to 1. For example, if we consider a starting value of 10, the returned sequence
is [10, 5, 16, 8, 4, 2, 1] Strengthen your code (error message should be “Oops”) and add
Python hints, docStrings and Comments to your submitted code.

'''

'''
5. Rewrite the body of the following function using a while loop. Strengthen your code
(error message should be “Oops”) and add Python hints, docStrings and Comments to
your submitted code.
 def chooseLargest(a,b):
results = []
list_len = len(a)
for i in range (list_len):
 results.append(max(a[i], b[i]))
return results
chooseLargest([1,2,3,4,5],[2,2,9,0,9])

'''
def chooseLargest(a,b):
    '''
    '''
    results =[]
    list_len = len(a)

    i=0
    while i < list_len:
        results.append(max(a[i],b[i]))
    
        i+=1
    return results

