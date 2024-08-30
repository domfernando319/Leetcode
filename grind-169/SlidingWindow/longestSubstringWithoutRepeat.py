class Solution:
    def longestSubstringWithoutRepeat(self, s: str):
        # Your code goes here
        if s is None or len(s) == 0:
            return 0

        i, j, maxLen = 0, 0, 0
        seen = set()

        while j < len(s):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            
            seen.add(s[j])
            maxLen = max(maxLen, j - i + 1)
            j += 1
        return maxLen


'''
Big O analysis:
Time: O(n)
    The sliding window optimizes the search space by eliminating substrings that are impossible
    this reduces time complexity from O(n^2) to O(N). once the j iterator reaches the end of the string the algorithm ends

Space : O(n) auxiliary space required because we used a set that will never contain more than n objects 

'''
