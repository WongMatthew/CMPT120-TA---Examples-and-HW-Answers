def checker(x):
    for j in range(2,x):
        if x % j == 0:
            return False
    return True

counter = 0
n = int(input('How many numbers do you want to check?\n'))

for i in range(n):
    integer = int(input('Enter a positive integer:\n'))
    
    if integer < 1:
        continue
        
    if integer < 0:
        print("PrimeFinder ignores negative numbers!")
    
    if checker(integer):
        print(integer, ' is a prime number.')
        counter+=1
    else:
        continue
print("Total prime numbers: ", counter)