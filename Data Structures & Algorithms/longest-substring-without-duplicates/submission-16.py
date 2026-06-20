class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0
        if len(s)==1:
            return 1
            
        # keep track of length longest substring so far
        longest = 0
       
        start = 0
        
        # create a set to keep track of letters and their indicies
        subSet = set()
        for i in range(len(s)):
            
            while s[i] in subSet:
                subSet.remove(s[start])
                start +=  1
            subSet.add(s[i])
            
            if (i - start +1) > longest:
                longest = i-start+1  

        return longest