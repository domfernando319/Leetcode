class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
            for each number num up to n: count number of 1s in binary representation of num

        '''
        for num in range(n):
            #convert num to binary
            # ex 3%2 = 1 1%2 = 1