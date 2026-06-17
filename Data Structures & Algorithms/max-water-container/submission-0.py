class Solution:
    def maxArea(self, heights: List[int]) -> int:
    
        left = 0
        right = len(heights)-1
        area = 0
        
        for i in range(len(heights)):
            if (right-left) * min(heights[left],heights[right]) > area:
                # update area
                area = (right-left) * min(heights[left],heights[right])
            
            # move the smaller pointer
            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return area

      