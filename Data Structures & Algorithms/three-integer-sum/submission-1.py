class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        output = []
        for i in range(len(sortedNums)):
            if i > 0 and sortedNums[i] == sortedNums[i-1]:
                continue
            l = i+1
            r = len(sortedNums)-1
            
            while l<r:
                triple = []
                currSum = sortedNums[i]+sortedNums[l]+sortedNums[r]
                if currSum == 0:
                    triple = [sortedNums[i],sortedNums[l],sortedNums[r]]
                    output.append(triple)
                    l += 1
                    r -= 1
                    while sortedNums[l] == sortedNums[l-1] and l<r:
                        l+=1
                elif currSum < 0:
                    l += 1
                else:
                    r -= 1

        return output
