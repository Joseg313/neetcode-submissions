class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        hashmap = {}


        for i, num in enumerate(nums):
            difference = target - num

            if difference in hashmap:
                answer.append(i)
                answer.append(hashmap[difference])
                return(sorted(answer))
            else:
                hashmap[num] = i
