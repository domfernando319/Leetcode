def fetchEveryOtherElement(array):
    i = 0
    while i < len(array):
        print(array[i])
        i += 2

def fetchEveryOtherElement2(array):
    if not array:
        print('no elements in the array')
        return
    for i in range(0, len(array), 2):
        print(array[i])
    print("DONE")

def fetchEveryOtherElement3(array):
    if not isinstance(array, list):
        raise ValueError('Input must be a list')
    result = [array[i] for i in range(0, len(array), 2)]
    print(result)

print("Test 1")
fetchEveryOtherElement([1,2,3,4,5,6,7,8])
print("Test 2")
fetchEveryOtherElement2([1,2,3,4,5,6,7,8])
print("Test 3")
fetchEveryOtherElement2([])
print("Test 4")
fetchEveryOtherElement3([])
print("Test 5")
fetchEveryOtherElement3([1,2,3,4,5,6,7,8])