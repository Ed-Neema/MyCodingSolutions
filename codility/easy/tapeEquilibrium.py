"""
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7
Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].
"""


def solution(A):
    least = 0                                    # O(1)
    for p in range(1, len(A)):                    # O(N)
        firstArray, secondArray = A[:p], A[p:]    # O(N)
        absDiff = abs(sum(firstArray) - sum(secondArray))  # O(N)
        if absDiff < least:                       # O(1)
            least = absDiff                       # O(1)
    return least                                  # O(1)


def optimalSolution(A):
    sum_of_left = 0                               # O(1)
    sum_of_right = sum(A)                          # O(n)
    best = None                                   # O(1)

    for P in range(0, len(A)-1):                # O(n)
        sum_of_left += A[P]                       # O(1)
        sum_of_right -= A[P]                      # O(1)
        difference = abs(sum_of_left - sum_of_right)  # O(1)
        # O(1)
        best = difference if best is None or difference < best else best

    return best                                     # O(1)
