#Print welcome statement 
print("Welcome! What would you like to do?" '\n')

#create functions for halfstring
def halfstring(word):
    length_of_word = len(word)
    if length_of_word % 2 == 0:
        print(word [length_of_word //2:])
    else:
        print('Please enter an even string.')
        
#create function for first three character
def first_three_character(x):
    length_of_x = len(x)
    if length_of_x <= 3:
        print (x)
    else:
        print(x [:3])

#print while loop
while True:
    print("[1] Enter 1 to print Half string.")
    print("[2] Enter 2 to print First three characters.")
    print("[q] Enter 'q' to print quit.")
    option = input('Enter your option:')
    if option == "1":
        string = input('Please input string of even length:')
        halfstring(string)
        print('\n')
    elif option == "q":
        print('See you later')
        break
    elif option == "2":
        string = input('Please enter a string:')
        if string != '':
            first_three_character(string)
        elif string == '':
            print("Empty string.")
        print('\n')