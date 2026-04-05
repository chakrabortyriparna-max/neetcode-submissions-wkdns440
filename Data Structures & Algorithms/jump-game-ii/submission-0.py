class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        # We continue as long as the right boundary hasn't reached the end
        while r < len(nums) - 1:
            farthest = 0
            # Explore all possibilities in the current jump range
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            
            # Move the window to the next range
            l = r + 1
            r = farthest
            res += 1
            
        return res