# Given a string, reverse it using iteration and recursion.


def reverse_string_iterative(str):
    stack = []
    for char in str:
        stack.append(char)

    str = ""
    for _ in range(len(stack)):
        str += stack.pop()

    return str

    # return str[::-1]


def reverse_string_recursive(str):
    if len(str) == 0:
        return str

    return reverse_string_recursive(str[1::]) + str[0]


def main():
    str = "yoyo mastery"

    print(reverse_string_iterative(str))

    print(reverse_string_recursive(str))


if __name__ == "__main__":
    main()
