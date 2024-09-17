class NumArray:

    def __init__(self, nums: List[int]):
        self.nums

    def sumRange(self, left: int, right: int) -> int:
        # use prefix sum to accumulate sum up to each index
        # the sum of the Range will be prefix[right] - prefix[left]
        #example: 1 3 4 5 8
        #         1 4 8 13 21
        # sumRange(1, 4) = prefix[4] - prefix[left - 1] = 21 - 1 = 20 inclusive!
        
        prefix = [0] * len(self.nums)
        prefix[0] = self.nums[0]
        res = None
        # O(n) aux space for creating prefix array
        # O(1) operation for calculating rangeSum
        for i in range(1, len(self.nums)):
            prefix[i] = prefix[i-1] + self.nums[i]
        if left == 0:
            return prefix[right]
        return prefix[right] - prefix[left - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)