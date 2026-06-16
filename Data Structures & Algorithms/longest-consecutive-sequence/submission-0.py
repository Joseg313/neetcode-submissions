class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnum = set(nums)

        longest = 0
        for num in setnum:
            # if a number does not have a number before it then it could be the start 
            #  of consescutive sequence
            if num-1 not in setnum:
                length = 1
                while ((num + length) in setnum):
                    length += 1
                
                if length > longest:
                    longest = length
        
        return longest