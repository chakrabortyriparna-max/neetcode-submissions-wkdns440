from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        q = deque()  # Stores indices
        
        for i in range(len(nums)):
            # Remove smaller values from the back of the deque
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            
            q.append(i)
            
            # Remove indices that are out of the window's range
            if q[0] < i - k + 1:
                q.popleft()
                
            # Once we've reached the first full window, start adding to results
            if i >= k - 1:
                res.append(nums[q[0]])
                
        return res
        