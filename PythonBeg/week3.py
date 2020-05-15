# Fancy greeting

# Odd-even
def odd_or_even():
    """ Tells user whether # is odd/even. """
    number = int(input("what number do you want me to examine? "))
    if (number % 2) == 0:
        print("that number is even. ")
    else:
        print("that number is odd. ")

# Grade Calculator
def grade_calculator():
    """ Converts numberic grades to letter grades."""
    percentage = int(input("what percent did the student get on the test? "))
    if percentage > 89:
        print("That student will get an A. ")
    elif percentage > 79:
        print("B")
    elif percentage > 69:
        print("C")
    elif percentage > 59:
        print("D")
    elif percentage > 49:
        print("E")
    elif percentage > 0:
        print("F")
