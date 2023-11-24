"""
Given an array of integers a, your task is to calculate the digits that occur the most number of times in the array. Return the array of these digits in ascending order.

Example

For a = [25, 2, 3, 57, 38, 41], the output should be solution(a) = [2, 3, 5].

Here are the number of times each digit appears in the array:

0 -> 0
1 -> 1
2 -> 2
3 -> 2
4 -> 1
5 -> 2
6 -> 0
7 -> 1
8 -> 1
The most number of times any number occurs in the array is 2, and the digits which appear 2 times are 2, 3 and 5. So the answer is [2, 3, 5].

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer a

An array of positive integers.

Guaranteed constraints:
1 ≤ a.length ≤ 103,
1 ≤ a[i] < 100.

[output] array.integer

The array of most frequently occurring digits, sorted in ascending order.
"""
# my trial
import math
def solution(a):
    # loop through the array
    # get all the individual digits
    singleDigitArray = []
    numberOfAppearances = []
    for numb in a:
        digits = getAllDigits(numb)
        singleDigitArray += digits
    # get the unique values in the singleDigitArray
    singleDigitArray = list(set(singleDigitArray))
    print("SingleDigit Array", singleDigitArray)
    # check number of appearance of each number
    for digit in singleDigitArray:
        occurrences = 0
        for numb in singleDigitArray:
            if numb == digit:
                occurrences+=1
        numberOfAppearances.append(occurrences)
    print("Number of Appearances", numberOfAppearances)
    sortedArray = []
    while len(numberOfAppearances) != 0:
        maxNumber = max(numberOfAppearances)
        indexNo = numberOfAppearances.index(maxNumber)
        print(singleDigitArray[indexNo])
        sortedArray.append(singleDigitArray[indexNo])
        numberOfAppearances.remove(maxNumber)
        singleDigitArray.remove(singleDigitArray[indexNo])
    
    return sortedArray
    
    
def getAllDigits(number):
    numberArray = []
    
    while number!= 0:
        remainder = number%10
        numberArray.append(remainder)
        number = math.floor(number/10)
    return numberArray




# my trial2
import math
def solution(a):
    # loop through the array
    # get all the individual digits
    singleDigitArray = []
    numberOfAppearances = []
    for numb in a:
        digits = getAllDigits(numb)
        singleDigitArray += digits
    # get the unique values in the singleDigitArray
    newDigitArray = list(set(singleDigitArray))
    print("SingleDigit Array", singleDigitArray)
    print("newDigitArray", newDigitArray)
    # check number of appearance of each number
    for digit in newDigitArray:
        occurrences = 0
        for numb in singleDigitArray:
            if numb == digit:
                occurrences+=1
        numberOfAppearances.append(occurrences)
    print("Number of Appearances", numberOfAppearances)
    sortedArray = []
    maxNumber = max(numberOfAppearances)
    print("maxNumber", maxNumber)
    numberOfMaxOccurence = numberOfAppearances.count(maxNumber)
    print("numberOfMaxOccurence", numberOfMaxOccurence)
    if numberOfMaxOccurence == 1:
        indexNo = numberOfAppearances.index(maxNumber)
        sortedArray.append(int(newDigitArray[indexNo]))
        return sortedArray
    else:
        for item in range(len(numberOfAppearances)):  
            if item == maxNumber:
                indexNo = numberOfAppearances.index(maxNumber)
                print(indexNo)
                sortedArray.append(int(newDigitArray[indexNo]))
                print("sortedArray",sortedArray)
                numberOfAppearances.remove(maxNumber)
                print("numberOfAppearances",numberOfAppearances)
                newDigitArray.remove(newDigitArray[indexNo])
                print("newDigitArray",newDigitArray)
        return sortedArray
                
    # while len(numberOfAppearances) != 0:
    #     maxNumber = max(numberOfAppearances)
    #     indexNo = numberOfAppearances.index(maxNumber)
    #     sortedArray.append(newDigitArray[indexNo])
        
    #     indexNo = numberOfAppearances.index(maxNumber)
    #     print(newDigitArray[indexNo])
    #     sortedArray.append(newDigitArray[indexNo])
    #     numberOfAppearances.remove(maxNumber)
    #     newDigitArray.remove(newDigitArray[indexNo])
    
    return sortedArray
    
    
def getAllDigits(number):
    numberArray = []
    
    while number!= 0:
        remainder = number%10
        numberArray.append(str(remainder))
        number = math.floor(number/10)
    return numberArray
