class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize max_sum with the first element
        max_sum = nums[0]
        current_sum = 0
        
        for n in nums:
            # If current_sum is negative, reset it to 0
            if current_sum < 0:
                current_sum = 0
            
            # Add current element to our running total
            current_sum += n
            
            # Update the global maximum if our current total is higher
            max_sum = max(max_sum, current_sum)
            
        return max_sum
        