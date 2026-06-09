class Solution:
    def isValid(self, s: str) -> bool:

        # automatically return false if there is an odd num of parentheses
        # because one of them is not closed
        if len(s) % 2 != 0:
            return False
        

        # dictionary storing what front parenthesis should equal
        symbolDict = {
            "[":"]",
            "(":")",
            "{":"}"
        }
        # # return false if s starts with a closing
        # if not s[0] in symbolDict:
        #     return False
        
        # create a heap element to stor open parenthis in order of appearance
        openings = []

        for i in range(len(s)):
            if s[i] in symbolDict:
                openings.append(s[i])
            else:
                try:
                    if symbolDict[openings.pop()] != s[i]:
                        return False
                except (KeyError, IndexError):
                    return False
        
        if len(openings) != 0:
            return False
        
        return True