# Recursion

# Rules
# 1. Identify base case
# 2. Identify recursive case
# 3. Return when needed

# Usually there are two returns, one for the base case and one for the recursive case.


# Anything that can be done recursively can be done iteratively.

# Recursion is dry and can make code more readable, however, it creates a large stack due to multiple function calls.

# Due to the large stack, recursion has a complexity of O(2^n). (This can be reduced to O(n) using Tail Call Optimization.)

# When to consider using
# Any time a tree is used or something is converted into a tree or for Divide and Conquer problems.
# I.e. use recursion when the problem,
#   1.  Can be divided into sub-problems that are smaller instances of the same problem
#   2. Has sub-problems identical in nature.
#   3. Has solutions of the sub-problems can be combined to solve it.


# Simple recursion example
def inception(counter):
    print(counter)

    if counter > 3:
        return "done"

    counter += 1
    return inception(counter)


def main():
    counter = 0

    print(inception(counter))


if __name__ == "__main__":
    main()
