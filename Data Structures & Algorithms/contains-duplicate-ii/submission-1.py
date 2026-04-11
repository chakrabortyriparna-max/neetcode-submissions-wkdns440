class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Map to store value -> last seen index
        seen = {}
        
        for i, n in enumerate(nums):
            # If we've seen this number before and it's within range k
            if n in seen and i - seen[n] <= k:
                return True
            
            # Update the map with the latest index
            seen[n] = i
            
        return False
