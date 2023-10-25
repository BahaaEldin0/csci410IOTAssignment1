def calculate_sum(*args):
    return sum(args)

def generate_fibonacci(N):
    fib_sequence = [0, 1]
    while len(fib_sequence) < N:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return ' '.join(map(str, fib_sequence))

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

def calculate_average(*args):
    return sum(args) / len(args)