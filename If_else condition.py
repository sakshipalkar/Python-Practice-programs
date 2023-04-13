calculation_of_hours = 24
name_of_unit = "hours"


def days_of_unit(no_of_days):
    print(type(no_of_days))# printing data type here
    if no_of_days > 0:
     return f"{no_of_days} days are {no_of_days * calculation_of_hours} {name_of_unit}"
    elif no_of_days == 0 :
     return ("you entered 0 input, please enter valid input")

def validate():#only for clean up purpose and called it globally
    if User_input.isdigit():
        # User_input_number=int(User_input)# int is for type casting
        calculated_value = days_of_unit(int(User_input))  # nestated function
        print(calculated_value)
    else:
        print("Your input is invalid,please enter valid number")


User_input=input("Hey user,Enter the no. of days I will convert it into hours!=")#input has by default string datatype
validate()