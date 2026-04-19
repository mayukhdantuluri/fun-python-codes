def fibonacci_iterative(n):
    a, b = 0, 1
    fib_sequence = []
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Example usage:
num_terms = int(input("Enter the number of terms for Fibonacci sequence: "))
if num_terms <= 0:
    print("Please enter a positive integer. Restart the program and try again, you dumbass.")
else:
    result = fibonacci_iterative(num_terms)
    print(f"First {num_terms} terms of Fibonacci Sequence: {result}")