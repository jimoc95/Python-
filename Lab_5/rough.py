
    # if numerical_grade is not an integer or number is not a string return error message
    if type(numerical_grade) !=int or type(number) !=str:
        return "Input value must be a number or a letter"

    # else if grade entered between 85 and 100 return "A"
    elif (numerical_grade >=85 and numerical_grade <=100):
        return "A"
    # else if number entered is "A" return "85-100"
    elif (number == "A"):
        return "85-100"

    # else if grade entered between 70 and 84 return "B"  
    elif (numerical_grade >=70 and numerical_grade <=84):
        return "B" 

    # else if number entered is "B" return "70-84"    
    elif (number == "B"):
        return "70-84"

    # else if grade entered between 55 and 69 return "C"    
    elif (numerical_grade >=55 and numerical_grade <=69):
        return "C"

    # else if number entered is "C" return "55-69"
    elif (number == "C"):
        return "55-69"

    # else if grade entered between 40 and 54 return "D"   
    elif (numerical_grade >=40 and numerical_grade <=54):
        return "D"

    # else if number entered is "D" return "40-54"
    elif (number == "D"):
        return "40-54"

    # else if grade entered between 25 and 39 return "E"    
    elif (numerical_grade >=25 and numerical_grade <=39):
        return "E"

    # else if number entered is "E" return "25-39"
    elif (number == "E"):
        return "25-39"

    # else if grade entered between 0 and 24 return "F" 
    elif (numerical_grade >=0 and numerical_grade <=24):
        return "F" 

    # else if number entered is "F" return "0-24"
    elif (number == "F"):
        return "0-24"

    # Otherwise return error message      
    else:
        return "Number entered, " + str(numerical_grade) + ", is outside of input values" 