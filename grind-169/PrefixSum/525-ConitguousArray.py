class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # 0 1 0
        # return 2 0,1 and 1,0
        # brute force: all combinations and check
        # interested in count of 0s and 1s

        zeros = 0
        ones = 0
        # map: ones - zeros -> i
        map = {}
        res= 0

        for (i, num) in enumerate(nums):
            if num == 1:
                ones += 1
            if num == 0:
                zeros +=1
            diff = ones - zeros
            if diff not in map:
                map[diff] = i
            
            if ones == zeros:
                #length of ones + zero
                res = ones + zeros
            else:
                res= max(res, i - map[diff])
        return res