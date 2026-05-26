class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ("".join(char for char in s if char.isalnum())).lower()

        n = len(cleaned_s)
        for i in range(int(round(n/2))):
            if cleaned_s[i] != cleaned_s[n-i-1]:
                return False
        
        return True