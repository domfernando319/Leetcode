from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
            non decreasing order. sorted 
            ex : 1 1 3 4 5 5 7
            modify in place. return number of unique elemts len(res)

            can use hashmap?
        '''
        map = Counter(nums)
        sortedMap = sorted(map.items())
        print(sortedMap)
        
        for i in range(len(sortedMap)):
            nums[i] = sortedMap[i][0]
            
        return len(sortedMap)
        