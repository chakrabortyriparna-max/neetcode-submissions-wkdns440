class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Use two pointers to compare characters from outside in
        l, r = 0, len(s) - 1
        
        while l < r:
            # Skip non-alphanumeric characters
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            
            # Compare lowercase versions of the characters
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
            
        return True
        