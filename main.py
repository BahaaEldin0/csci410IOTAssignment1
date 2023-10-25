def calculate_sum(*args):
    return sum(args)

def generate_fibonacci(N):
    fib_sequence = [0, 1]
    while len(fib_sequence) < N:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return ' '.join(map(str, fib_sequence))
