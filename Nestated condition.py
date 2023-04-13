calculation_of_hours = 24
name_of_unit = "hours"


def days_of_unit(no_of_days):
   return f"{no_of_days} days are {no_of_days * calculation_of_hours} {name_of_unit}"

User_input=input("Hey user,Enter the no. of days I will convert it into hours!=")#input has by default string datatype
#User_input_number=int(User_input)
calculated_value=days_of_unit(int(User_input))#nestated function
print(calculated_value)