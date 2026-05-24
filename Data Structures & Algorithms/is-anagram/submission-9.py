class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not sorted(s) == sorted(t):
            return False

        return True
        