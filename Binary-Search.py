def binarySearch(sortedList, item):
    low = 0
    high = len(sortedList) - 1

    while low < high :
        mid = (low + high) // 2
        guess = sortedList[mid]
        if guess == item :
            return mid 
        if guess > item :
            high = mid -1
        else:
            low = mid + 1
    return -1

mylist = [1, -2,3,4,5]
print(binarySearch(mylist, 3))