from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Map character count tuple to list of strings
        res = defaultdict(list)

        for s in strs:
            # Create a count array for 26 lowercase English letters
            count = [0] * 26
            
            for char in s:
                # Map 'a' -> 0, 'b' -> 1, ..., 'z' -> 25
                count[ord(char) - ord('a')] += 1
            
            # Convert list to tuple to use as dictionary key
            res[tuple(count)].append(s)
            
        return list(res.values())
        