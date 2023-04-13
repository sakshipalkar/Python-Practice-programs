calculation_of_hours = 24
name_of_unit = "hours"


def days_of_unit(no_of_days):
   return f"{no_of_days} days are {no_of_days * calculation_of_hours} {name_of_unit}"


my_var=days_of_unit(35)
print(my_var)#simply printing the hours value