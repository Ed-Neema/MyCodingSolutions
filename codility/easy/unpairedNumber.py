"""

A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.
"""

"""
[9, 3, 9, 3, 9, 7, 9]
[3, 3, 7, 9, 9, 9, 9]
"""
"""
#edge cases:
1. No items in the array
2. Once item
"""


def solution(A):
    newarray = []
    for i in range(len(A)):
        removed = A.pop()
        if removed in newarray:
            newarray.remove(removed)
        else:
            newarray.append(removed)

    if len(newarray) == 0:
        return 0

    return newarray[0]

"""
The above code has a time complexity of O(N^2) because of the pop() method. 
The pop() method has a time complexity of O(N) because it has to shift the elements in the array.
How can we improve this? 

"""


def solution(A):
    seen = set()

    for element in A:
        if element in seen:
            seen.remove(element)
        else:
            seen.add(element)

    if seen:
        return seen.pop()

    return 0

"""
Here's why this approach is considered better:

Efficient Lookup: Sets provide constant-time lookup, which means checking if an element is in a set takes the same amount of time regardless of the size of the set. This is because sets use a hash table internally to store elements, allowing for fast retrieval.

Handling Duplicates: The code handles duplicate numbers correctly. When a duplicate number is encountered, it is removed from the set. This ensures that the set only contains unpaired numbers.

Space Efficiency: The set data structure allows for efficient storage of unique elements. In this case, it is used to store the unpaired numbers. Since the set only contains unique elements, it avoids storing unnecessary duplicates.

Simplicity: The code is relatively simple and easy to understand. It iterates over the list of numbers, adding each number to the set if it hasn't been seen before, and removing it if it has been seen. Finally, it returns the remaining element in the set, which is the unpaired number.
"""