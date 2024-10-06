class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        use while loop or similar to check bound or visited
        move left and right bounds after traversing the perimeter

        Time: O(m*n) where m is num of rows and n is num of cols
        Space: O(1) excluding return array O(m*n) including it
        '''

        if not matrix:
            return []
        ROWS = len(matrix)
        COLS = len(matrix[0])

        result = []

        left, right, top, bottom = 0, COLS - 1, 0, ROWS -1

        while left <= right and top <= bottom:
            #traverse left to right across top
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left +=1 
            
        return result