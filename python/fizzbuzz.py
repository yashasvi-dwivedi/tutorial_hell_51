def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "fizzbuzz"
    if n % 3 == 0:
        return "fizz"
    if n % 5 == 0:
        return "buzz"


# Test cases
if __name__ == "__main__":
    print(fizzbuzz(15))
    print(fizzbuzz(3))
    print(fizzbuzz(5))
