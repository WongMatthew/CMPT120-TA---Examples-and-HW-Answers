def is_prime(n):
    if n < 2:
        return False
    for i in range(2, x):
        if n % i == 0:
            return False
    return True

def prime_divisors(n):
    count = 0
    for i in range(2, n+1):
        if is_prime(i) and n % i == 0:
            count += 1
    return count

def prime_numbers_less_than(n):
    count = 0
    for i in range(2, n):
        if is_prime(i):
            count += 1
    return count

n = int(input("Enter the number of products: "))
total_price = 0

for i in range(n):
    weight = int(input(f"Enter the weight of product {i+1}: "))
    if is_prime(weight):
        price = prime_numbers_less_than(weight)
    else:
        price = prime_divisors(weight)
    total_price += price

if is_prime(total_price):
    discount = prime_numbers_less_than(total_price)
else:
    discount = prime_divisors(total_price)

final_price = total_price - discount
print(f"The total price is ${total_price}, and the discount is ${discount}. The final price is ${final_price}.")