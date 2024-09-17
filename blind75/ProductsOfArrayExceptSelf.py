class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # naive implementation prefix and postfix
        # [1 2 4 6]
        # 
        
        prefix = [1] * (len(nums) + 2)
        postfix = [1] * (len(nums) + 2)
        result = [1] * (len(nums) + 2)
        
        for (i,e) in enumerate(nums):
            j = i + 1
            prefix[j] = nums[i] * prefix[j-1]

        revArr = nums[:: -1]
        for (i,e) in enumerate(revArr):
            j = i + 1
            postfix[j] = revArr[i] * postfix[j-1]
        postfix = postfix[:: -1]

        for i in range(1 , len(result) - 1):
            result[i] = prefix[i-1] * postfix[i+1]
        
        return result[1: len(result) - 1]

'''
Time: O(N) although were using several loops the average we still iterate through input n times
     3 loops: O(3n) -> O(n)
Space: O(n) <- 3 axuliary spaces each holding at most n items

Improvements:
    * reversing array is not a problem 0(n) 
    * use less aux space. i dont need 3 arrays. You can use in place approach to use one array for result


'''