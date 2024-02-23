# Bubble sort

# Elementary sorting algorithms: bubble, insertion, selection

# Bubble sort comes from the idea of "bubbling up", the first value is compared with the second value and swaps places depending on the value comparisons.

# Bubble sort is a simple sorting algorithm but has one of the worst time complexities on average due to the nested for-loops.

# Complexities: Time (best, average, worst): Ω(n), Θ(n^2), O(n^2) / Space: O(1)


def bubbleSort(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]


def main():
    numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    print(numbers)

    bubbleSort(numbers)
    print(numbers)


if __name__ == "__main__":
    main()
