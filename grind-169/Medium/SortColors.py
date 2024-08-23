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
                   
            