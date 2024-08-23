class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        nextNonZeroIndex = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                #swap 
                nums[i], nums[nextNonZeroIndex] = nums[nextNonZeroIndex], nums[i]
                nextNonZeroIndex += 1
            print(nums)
            
        return nums