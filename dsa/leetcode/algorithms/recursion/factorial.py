# Comparing a for loop and a recursive function that both evaluate the factorial of any number


def find_factorial_recursive(number):
    """
    Evaluating the factorial of some number recursively.
    """
    if number == 1:
        return number

    return find_factorial_recursive(number - 1) * number


def find_factorial_iterative(number):
    """
    Evaluating the factorial of some number iteratively.
    """
    result = 1
    for i in range(2, number + 1):
        result *= i

    return result


def main():
    print("Factorial of 7 recursively:", find_factorial_recursive(7))

    print("Factorial of 7 iteratively:", find_factorial_iterative(7))


if __name__ == "__main__":
    main()
