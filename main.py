#Done Bahaa Eldin Moustafa 202000498
def calculate_sum(*args):   
    return sum(args)

def generate_fibonacci(N):
    fib_sequence = [0, 1]
    while len(fib_sequence) < N:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return ' '.join(map(str, fib_sequence))


#Done Anas Hany Kamal 19100081

def check_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def reverse_string(input_string):
    return input_string[::-1]


#Done Abdelrahman Atrozy 202001188
def calculate_average(*args):
    return sum(args) / len(args)

def count_vowels(input_string):
    vowels = "AEIOUaeiou"
    return sum(input_string.count(vowel) for vowel in vowels)


#Done Mohamed Ahmed Mohamed 202000991

def prime_factorization(number):
    factors = []
    divisor = 2
    while number > 1:
        if number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        else:
            divisor += 1
    return factors

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a