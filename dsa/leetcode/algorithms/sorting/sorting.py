# Sorting

# As more and more data is being handled, sorting and searching are two of the biggest computer science problems.

# A languages built-in sorting functions are good for programs with small input data (see Python sort method used in main).

# With very large datasets, sorting becomes very costly and built-in sorting functions become insufficient requiring custom sorting methods and/or data preprocessing.

# Useful sorting algorithms and there complexities
# Space/Time Complexities https://www.bigocheatsheet.com/
# Visual sorting: https://www.toptal.com/developers/sorting-algorithms
#   - Radix Sort
#   - Quick Sort
#   - Heap Sort
#   - Bubble Sort
#   - Selection Sort
#   - Insertion Sort
#   - Merge Sort
#   - Counting Sort


def main():
    # unsorted
    letters = ["a", "d,", "z", "e", "r", "b"]
    print(letters)

    # sorted
    letters.sort()
    print(letters)

    # Some languages sort by ASCII code (e.g. JavaScript), Python performs sort on lists differently, see https://docs.python.org/3/howto/sorting.html

    basket = [2, 65, 34, 2, 1, 7, 8]
    print(basket)

    basket.sort()
    print(basket)
    # JavaScript would return [1, 2, 2, 34, 65, 7, 8]

    spanish = ["único", "árbol", "cosas", "fútbol"]
    print(spanish)

    spanish.sort()
    print(spanish)
    # Python returns ['cosas', 'fútbol', 'árbol', 'único']

    # Sort in JavaScript
    # JavaScript sort provides an argument that takes a function to instruct the sorting algorithm on how to sort.

    # Passing a function to this sort method that returns `a.localCompare(b)`
    # sorts as expected ['árbol', 'cosas', 'fútbol', 'único']
    """
    // JavaScript sort
    // see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare

    spanish.sort(function(a, b) {
        return a.localCompare(b);

        // to return `basket` in order, the following can be returned
        // return a - b 
    })
    """


if __name__ == "__main__":
    main()
