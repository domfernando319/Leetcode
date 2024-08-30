class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # THINK Pointers as REGIONS!!!
        # idea of partitioning the array
        # Buckets: 0's | 1's | 2's

        left = 0
        right = len(nums) - 1
        i = 0

        while ( i <= right):
            if nums[i] == 0:
                nums[i], nums[left] = nums[left] , nums[i]
                left += 1
                i+= 1
            elif nums[i] == 1:
                i+= 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
                   

'''
Big O Analysis:
If nums[i] is 0, it is swapped with nums[left], 
and both left and i are incremented.

If nums[i] is 1, just increment i.

If nums[i] is 2, it is swapped with nums[right], 
and right is decremented.
i is not incremented in this case because the swapped value needs to be evaluated again

Best Case: O(n) 2s are already in place
Worst Case: O(2n) -> O(n) each swap requires a reprocess 


 If you need to sort an array with more than three distinct colors or categories, 
 the partitioning approach does become more complex.
 Here’s a breakdown of the different strategies and their implications:

1. Using a HashMap or Dictionary
For an arbitrary number of colors, a hashmap (or dictionary) can indeed simplify the problem:

Algorithm:
Traverse the array and count the occurrences of each color using a hashmap.
Rebuild Array: Iterate over the hashmap and reconstruct the array based on the counts.

Time Complexity: O(n)

Space Complexity: O(n)




'''