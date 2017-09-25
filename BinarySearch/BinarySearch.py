# Binary Search algorithm is a search algorithm that finds the position of a target value within a sorted array.

def binarySearch(searchValue, list) -> bool:
    sortedList = sorted(list)

    lowerIndex = 0
    upperIndex = len(sortedList) - 1

    while lowerIndex <= upperIndex:

        middleIndex = (upperIndex + lowerIndex) // 2
        middleValue = sortedList[middleIndex]

        if searchValue == middleValue:
            return True
        elif searchValue < middleValue:
            upperIndex = middleIndex - 1
        elif searchValue > middleValue:
            lowerIndex = middleIndex + 1
    return False
