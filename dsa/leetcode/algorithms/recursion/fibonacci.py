# Given a number N return the index of the Fibonacci sequence, where the sequence is:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
# the pattern of the sequence is that each value is the sum of the 2 previous values, that means that for N = 5 -> 2 + 3


def fibonacci_iterative(n):
    if n == 0:
        return 0

    fibonacci_sequence = [0, 1]
    if n == 1:
        return 1

    for i in range(1, n):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i])

    return fibonacci_sequence[n]


def fibonacci_recursive(n):
    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def main():
    n = 12

    print(f"{n}-Fibonacci iteratively", end=": ")
    for i in range(n + 1):
        print(fibonacci_iterative(i), end=", ")

    print()

    print(f"{n}-Fibonacci recursively", end=": ")
    for i in range(n + 1):
        print(fibonacci_recursive(i), end=", ")

    print()


if __name__ == "__main__":
    main()
