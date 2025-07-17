def fibonacciSequence(n):
    count = {}
    for i in range(n):
        if i == 0:
            count[i] = 0
        elif i == 1:
            count[i] = 1
        else:
            count[i] = count[i - 1] + count[i - 2]
    return count


# Example usage:
if __name__ == "__main__":
    n = 10
    fib_sequence = fibonacciSequence(n)
    print(f"Fibonacci sequence up to {n} terms: {fib_sequence}")
    n = 0
    fib_sequence = fibonacciSequence(n)
    print(f"Fibonacci sequence up to {n} terms: {fib_sequence}")
    n = 1
    fib_sequence = fibonacciSequence(n)
    print(f"Fibonacci sequence up to {n} terms: {fib_sequence}")
    n = 5
    fib_sequence = fibonacciSequence(n)
    print(f"Fibonacci sequence up to {n} terms: {fib_sequence}")
