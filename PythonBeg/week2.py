# Temperature Converter
def ctof():
    """ Changes Celsius to Fahrenheit. """
    c = input("How many degrees celsius? ")
    f = int(c) * 1.8 + 32

    print(c + " degrees celsius is " + str(f) + " degrees fahrenheit! ")

# Height Converter
def height_converter():
    """ Changes height in cm to height in ft and inches. """
    cm = int(input("How tall are you in cm? "))
    inches = cm * 0.3937
    ft = inches // 12
    rem_inches = inches % 12
    p	rint("You are " + str(int(ft)) + "ft and " + str(round(rem_inches)) + "in.")

# Average
def average():
    """ Gets the average of three numbers. """
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    num3 = int(input("Enter num3: "))
    average = (num1 + num2 + num3) / 3
    print("The average is " + str(average))
