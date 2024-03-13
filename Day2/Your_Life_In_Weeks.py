# Consider you are gonna live for 77 Years
# How many days,weeks and months are left in your life

age=input("What is your current age:")

# Considering having 365 Days in year 
age_left=77-int(age)
days_left=age_left*365
months_left=age_left*12
weeks_left=age_left*52
print(f"Number of Days Left are: {days_left}, Months Left are: {months_left}, Weeks Left are: {weeks_left}")
