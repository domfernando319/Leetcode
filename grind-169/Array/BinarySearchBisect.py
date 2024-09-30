import bisect

def binary_search_left(arr, target):
    index = bisect.bisect_left(arr, target)
    if index < len(arr) and arr[index] == target:
        return index
    return -1  # Target not found

# Example usage
sorted_list = [1, 2, 4, 4, 5, 6]
target = 4
result = binary_search_left(sorted_list, target)
print(result)  # Output: 2 (index of the first occurrence of 4)
