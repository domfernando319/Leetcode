class Solution:
    def max_area(self, heights):
        #two pointer solution
        left = 0
        right = len(heights) - 1
        maxArea = 0  # set max area to 0
        while left < right: # while not equal or crossing
            # calculate area
            area = (right - left) * min(heights[left], heights[right]) 
            maxArea = max(maxArea, area)
            
            if heights[left] < heights[right]:
                left += 1

            else:
                right -= 1

        return maxArea

