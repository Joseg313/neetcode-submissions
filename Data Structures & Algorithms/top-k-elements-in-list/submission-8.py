class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        buckets = [[] for i in range(len(nums) + 1)]
        answer = []
        #created frequency hash map
        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)

        #create bucket sort
        for num, count in frequency.items():
            buckets[count].append(num)

        #extract the k highest values and append to answer
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                answer.append(num)
                if len(answer) == k:
                    return answer