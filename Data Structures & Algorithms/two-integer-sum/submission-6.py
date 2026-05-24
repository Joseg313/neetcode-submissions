class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i in range(len(nums)):
            
            for j in range(len(nums)-i-1):
                if nums[i] + nums[j+1+i] == target:
                    answer.append(i)
                    answer.append(j+1+i)
                    print(answer)
                    return sorted(answer)
