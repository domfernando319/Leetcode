class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # first idea is to sort but we cannot modify array
        # track last time we saw the integer -> no uses hashmap
        # two ptrs
        # prefix sum
        # 3 1 3 4 2
        # 3 4 7 11 13
        # floyds algorithm cycle detection using a linked list approach

        #phase 1

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        #phase 2 of algo
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow