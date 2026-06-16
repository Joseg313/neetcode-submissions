class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 != 0:
            return False

        pairs = {
            "[":"]",
            "(":")",
            "{":"}",
        }

        openings = []
        for i in range(len(s)):
            if s[i] in pairs:
                openings.append(s[i])
            else:
                if not (len(openings)):
                    return False
                if pairs[openings.pop()] != s[i]:
                    return False
                
        if len(openings):
            return False

        return True
