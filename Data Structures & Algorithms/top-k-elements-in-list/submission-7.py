class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        answer = []
        
        n = len(nums)
        buckets = [[] for _ in range(1+n)]
        
        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)
        
        for num, count in frequency.items():
            buckets[count].append(num)
        
        answer = []
        for i in range(len(buckets) -1, 0, -1):
            for num in buckets[i]:
                answer.append(num)
                if len(answer) == k:
                    return answer


        # count each number and rank then index that list to return the 
        # k top of the list
        
        '''
        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)

        
        print(frequency)
        
        print(sorted(frequency, key=frequency.get))
        return sorted(frequency, key=frequency.get)[-k:]
        '''