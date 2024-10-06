def findIndexOfTarget(array, target):
    for el in array:
        if el == target:
            print(array.index(el))
            return array.index(el)
    print(-1)
    return -1

print("Test 1")
findIndexOfTarget([1,2,3,4,5,6], 4) # should return 3
print("Test 2")
findIndexOfTarget([], 2) # should return -1
print("Test 3")
findIndexOfTarget([1,3,5,7], 2) # should return -1

