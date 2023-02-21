# hello user!
print("Hello user!")
# take in user input
date = input("Enter a date in the format mm-dd-yyyy: ")
# split user input at -
month, day, year = date.split("-")
# take each number and modify it

# month --> []
months = ['January','February','March','April','May','June','July','August','September','October','November','December']
month_name = months[int(month)-1]

# f strings
# print(month + day + year)
# print(month_name, str(int(day)), str(year))
print(f"{month_name} {day}, {year}")