def MagiCal(n):
  for i in range(n):

    calc = (input(
      'Select the operator from the list of Addition (1), Subtraction (2), Multiplication (3), Division (4):\n'
    ))

    if calc not in ['1', '2', '3', '4']:
      print('Invalid input!')
      continue

    first_number = int(
      input('Enter the first number in the interval of [0,100]:\n'))
    second_number = int(
      input('Enter the second number in the interval of [0,100]:\n'))

    if first_number > 100 or first_number < 0 or second_number > 100 or second_number < 0:
      print('Magic calculator can not perform your operation!')
      continue

    if calc == '1':
      print(first_number, '+', second_number, '=',
            first_number + second_number)
    elif calc == '2':
      print(first_number, '-', second_number, '=',
            first_number - second_number)

    elif calc == '3':
      print(first_number, '*', second_number, '=',
            first_number * second_number)

    elif calc == '4':
      if second_number == 0:
        print('The denominator cannot be 0.')
      else:
        print(first_number, '/', second_number, '=',
              first_number / second_number)


n = int(input('Hi, how many operations do you want MagiCal to perform?\n'))
MagiCal(n)