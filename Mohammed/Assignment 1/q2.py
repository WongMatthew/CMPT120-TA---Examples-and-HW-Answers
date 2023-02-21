k = int(input('Hi, how many operations do you want MagiCal to perform?\n'))
for i in range(k):  
    operator = (input('Select the operator from the list of Addition (1), Subtraction (2), Multiplication (3), Division (4):\n'))
    if operator not in ["1", "2", "3", "4"]:
        print('Invalid input!')
        continue    
    try:
        first_number = int(input('Enter the first number in the interval of [0,100]:\n'))
    except ValueError:
        print('Magic calculator can not perform your operation!')
        continue
    try:
        second_number = int(input('Enter the second number in the interval of [0,100]:\n'))
    except ValueError:
        print('Magic calculator can not perform your operation!')
        continue
    if first_number < 0 or first_number > 100 or second_number < 0 or second_number > 100:
        print('Magic calculator can not perform your operation!')
        continue 
    if operator == 4 and second_number == 0:
        print('The denominator cannot be 0.')
        continue
    if operator == "1":
        result = float(first_number + second_number)
        print(first_number, '+', second_number, '=', result)
    elif operator == "2":
        result = float(first_number - second_number)
        print(first_number, '-', second_number, '=', result)
    elif operator == "3":
        result = float(first_number * second_number)
        print(first_number, '*', second_number, '=', result)
    elif operator == "4":
        result = float(first_number / second_number)
        print(first_number, '/', second_number, '=', result)