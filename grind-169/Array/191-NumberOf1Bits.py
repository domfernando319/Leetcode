class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
            mod right most digit by 2 to determine if there is a 1 or not
        '''

        res = 0
        while n:
            if n%2 == 1:
                res += 1
            n = n >> 1

        return res
