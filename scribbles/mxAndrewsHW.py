"""
    Defining your python script as a function
    this function requests the programmer give a
    "daysInYear" variable (See line 39)
"""
def isYearALeapYear(daysInYear):

    daysPerYear = 365
    daysPerLeapYear = 366
    monthsPerYear = 12
    daysPerMonth = 31
    hoursInDay = 24
    minsInHour = 60
    secsInMin = 60

    regYearResult = daysPerYear * hoursInDay * minsInHour * secsInMin

    leapYearResult = daysPerLeapYear * hoursInDay * minsInHour * secsInMin

    if daysInYear == daysPerLeapYear:
        print( "There are", leapYearResult, "seconds in this year", )
    elif daysInYear == daysPerLeapYear:
        print( f"There are {leapYearResult} seconds in this year", )


"""
    The main function. If you run:

    python3 mxAndrewsHW.py

    in the terminal, it will run the function below automatically
"""
if __name__ == "__main__":

    userInput = int(input ( "How many days are there this year? "))

    # running the function we defined above
    # Putting in userInput for daysInYear in the above function.
    isYearALeapYear(userInput)

