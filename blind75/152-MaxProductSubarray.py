class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        brute force is check every subarray combination and calculate product
        then get max. Brute force is O(n^2)
        what patterns do we look for?
        All positive numbers -> product will increasing
        all negative -> sign alternates
        compute product for first two elements and branch out 
        keep track of min and max prod subarray
        edge case: any 0s will ruin this approach
        what do we do? filter out zeros? can we do it O(n)?
        No we cant remove 0s. we need them to maintain unique subarray and not interfere with each other

        '''


        res = nums[0]
        currMax = 1
        currMin = 1
        # 1 2 -3 4
        # 1 2  
        #-1-2
        for i in nums:
            temp = currMax
            
            currMax = max(currMin * i, currMax * i, i) 
            currMin = min(currMin * i, temp * i, i)
            res = max(currMax, res)
        return res

