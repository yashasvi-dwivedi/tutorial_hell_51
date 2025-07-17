def factorialCaculator(n):
    if n < 0:
        return "undefined"
    if n == 0:
        return 1
    for i in range(n - 1, 0, -1):
        n *= i
    return n


# Test cases
if __name__ == "__main__":
    print(factorialCaculator(5))  # Output: 120
    print(factorialCaculator(0))  # Output: 1
    print(factorialCaculator(-3))  # Output: "undefined"
