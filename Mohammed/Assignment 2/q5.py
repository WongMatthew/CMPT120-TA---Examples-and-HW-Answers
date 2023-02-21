def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(numbers):
    result = 1
    for number in numbers:
        result = (result * number) // gcd(result, number)
    return result

n = int(input("Enter the number of denominators: "))
denominators = []
for i in range(n):
    while True:
        denominator = int(input(f"Enter the denominator {i+1}: "))
        if denominator > 0:
            denominators.append(denominator)
            break
        else:
            print("Invalid input. Please enter a positive integer.")
lcm_result = lcm(denominators)
print(f"The least common multiple of {denominators} is: {lcm_result}")