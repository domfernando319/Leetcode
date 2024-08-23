class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums array ie [2,7,11, 15]
        # assume exactly one solution in each array
        # you cannot use the same element twice

        enums = [] # to store enumerated nums
        for (i, e) in enumerate(nums):
            enums.append((e,i))
        
        enums.sort() # check to see if default sort is by first index
                
        left = 0
        right = len(enums) -1 
        res = []
        
        while (left < right):
            if enums[left][0] + enums[right][0] == target:
                res = [enums[left][1], enums[right][1]]
                return res
            elif enums[left][0] + enums[right][0] < target:
                left += 1
            else:
                right -= 1

        return res