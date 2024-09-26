class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        O(n) solution: for each element if you see an element check if exists in hashmap
        add it with count 1 or increment count
        Use a list to track count of n in 0th index, and n in the 1st index
        this will allow us to sort the values of the map in nlogn
        '''
        map = defaultdict(list)
        print(map)
        for n in nums: # O(n)
            if n not in map.keys():
                map[n] = [1, n]
            else:
                map[n][0] += 1
            
        sortedFreq = sorted(map.values()) # O(nlogn)

        res = []
        for i in range(k): #O(nlogn)
            arr= sortedFreq.pop() #[3,1 ]
            res.append(arr[1])

        return res
    
from collections import Counter 
import heapq
class Solution2:
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        
        '''
        from collections import Counter

        nums = [1, 1, 2, 3, 2, 2, 4]
        freq_map = Counter(nums) -> Counter({2: 3, 1: 2, 3: 1, 4: 1})

        '''

        # Step 1: Count frequencies of each element
        freq_map = Counter(nums)
        
        # Step 2: Use a max-heap (simulated by pushing negative frequencies)
        max_heap = []
        
        for num, freq in freq_map.items():
            # Push negative frequency to simulate max-heap
            heapq.heappush(max_heap, (-freq, num))
        
        # Step 3: Pop the k most frequent elements
        top_k = []
        for _ in range(k):
            freq, num = heapq.heappop(max_heap)
            top_k.append(num)
        
        return top_k
       
       
       
       
       
       
       
        