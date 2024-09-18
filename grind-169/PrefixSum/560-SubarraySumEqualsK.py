class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        '''
          1 3 6

          111 k = 2     [1,1] [1,1]

          Check differences of prefix sums against k?
          sumAtI - sumAtJ = k -> that subarray from i-j sums to k
          Map: {prefixSum => count that particular prefixSum occurs}
          prefixSum - k = j

        '''

        if not nums:
            return 0
        
        prefixSums = {0:1}

        currSum = 0
        count = 0

        for num in nums:
            currSum += num
            diff = currSum -k

            count += prefixSums.get(diff, 0) # return 0 if diff does not exist
            prefixSums[currSum] = 1 + prefixSums.get(currSum, 0)
            
        return count