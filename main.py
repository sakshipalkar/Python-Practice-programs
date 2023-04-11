print(1)
print("200")  # double quote and single quote can be used
print('200')
print("20 day are " + str(50) + " minutes")
print(f"20 days are {50} minutes")  # f is used formating
print(f"20 days are {20 * 24 * 60} minutes")  # how many minutes in 20 days
print(f"30 days are {30 * 24 * 60 * 60} seconds")  # how many second in 30 days
calculation_of_sec = 24 * 60 * 60
name_of_units = "seconds"
print(f"30 days are {30 * calculation_of_sec} seconds")
print(f"30 days are {30 * calculation_of_sec} {name_of_units}")
#function
calculation_of_hours = 24
name_of_unit = "hours"


def days_of_unit(no_of_days):
    print(f"{no_of_days} days are {no_of_days * calculation_of_hours} {name_of_unit}")
    print("All is well!")


days_of_unit(20)
days_of_unit(78)




