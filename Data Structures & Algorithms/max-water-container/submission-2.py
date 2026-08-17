class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # Logic:
        # Formula: max = (right - left) * min(heights[right], heights[left])
        # 1. Two pointers, left = 0, right = size - 1
        # 2. Do calculation
        # 3. Left += 1
        # 4. Do calculation
        # 5. Right -= 1
        # 6. Do calculation
        # 7. Return max

        size = len(heights)
        i, j = 0, size - 1
        maxArea = 0

        while i <= j:
            
            temp = abs(i-j) * min(heights[i], heights[j])
            maxArea = max(maxArea, temp)
            if heights[i] >= heights[j]:
                j-=1
            else:
                i+=1
            
            


        return maxArea
