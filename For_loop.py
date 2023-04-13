calculation_of_hours = 24
name_of_unit = "hours"


def days_of_unit(no_of_days):
    return f"{no_of_days} days are {no_of_days * calculation_of_hours} {name_of_unit}"


def validate():
    try:
        user_input_number = int(number_of_days)
        if user_input_number > 0:
            calculated_value = days_of_unit(user_input_number)  # nestated function
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered 0 input, please enter valid input")
        else:
            print("Your input is negative number,please enter valid number")

    except ValueError:
        print("Your input is invalid,please enter valid number")


User_input = " "
while User_input != "exit":  # True can be used to continue get user input until we stop program manually.
    User_input = input(
        "Hey user,Enter the no. of days I will convert it into hours!=")  # input has by default string datatype
    print(type(User_input.split(",")))# Printing data type
    print(User_input.split(","))
    for number_of_days in User_input.split(","):#it is type conversation by default string to list
        validate()
# User take input as a list
