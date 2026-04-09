class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0
        
        while l < r:
            # Calculate width and the limiting height
            width = r - l
            current_height = min(heights[l], heights[r])
            
            # Update the maximum area found so far
            max_area = max(max_area, width * current_height)
            
            # Move the pointer that points to the shorter bar
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
                
        return max_area