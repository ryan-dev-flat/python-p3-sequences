#!/usr/bin/env python3
def print_fibonacci(length):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < length:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    print(fibonacci_sequence[:length])

