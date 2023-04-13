def days_of_unit(no_of_days, convertion_unit):
    if convertion_unit == "Hours":
        return f"{no_of_days} days are {no_of_days * 24} Hours"
    elif convertion_unit == "Minutes":
        return f"{no_of_days} days are {no_of_days * 24 * 60} Minutes"
    else:
        return "unsupported unit"


def validate():
    try:
        user_input_number = int(Value_and_Units_dictionary["Days"])
        if user_input_number > 0:
            calculated_value = days_of_unit(user_input_number, Value_and_Units_dictionary["Unit"])  # nestated function
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
        "Hey user,Enter the no. of days and hours!=")  # input has by default string datatype
    Value_and_Units = User_input.split(":")
    Value_and_Units_dictionary = {"Days": Value_and_Units[0], "Unit": Value_and_Units[1]}
    validate()
