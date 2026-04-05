class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        # Fill the hash map with counts from s
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # Subtract counts using string t
        for char in t:
            if char not in count:
                return False  # t has a character s doesn't have
            count[char] -= 1
            
            if count[char] < 0:
                return False # t has more of this character than s does

        return True
