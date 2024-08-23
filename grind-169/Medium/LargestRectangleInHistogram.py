class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        while (stack):
            poppedI, poppedE = stack.pop()
            width = len(heights) - poppedI
            maxArea = max(maxArea, width * poppedE)

        return maxArea

     
        
        