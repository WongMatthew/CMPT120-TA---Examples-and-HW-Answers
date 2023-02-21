print('Hello user!')

# Ask the user for a location
location = input('Please input your city, provice, and country: ')

# Split the input into its components
city, province, country = [part.strip() for part in location.split(',')]

# Get the first letter of each component and join them with dots
initials = '.'.join([city[0], province[0], country[0]])

# Display the initials
print(initials)