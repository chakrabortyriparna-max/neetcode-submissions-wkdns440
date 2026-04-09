class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0
        stack = [] # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            # If current height is lower than the top of the stack, 
            # we must pop and calculate areas
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                # The current bar can start from the index of the popped bar
                start = index
            stack.append((start, h))

        # Calculate area for remaining bars in the stack
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
            
        return max_area