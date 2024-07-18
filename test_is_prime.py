"""
Testing function that checks whether a number is prime or not
"""

def check_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


print(check_prime(2))
print(check_prime(61))
print(check_prime(44))
print(check_prime(1000))
print(check_prime(837))
