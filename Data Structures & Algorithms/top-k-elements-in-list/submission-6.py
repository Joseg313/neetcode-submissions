class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        answer = []
        # count each number and rank then index that list to return the 
        # k top of the list

        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)

        
        print(frequency)
        
        print(sorted(frequency, key=frequency.get))
        return sorted(frequency, key=frequency.get)[-k:]
        '''
        for count in range(k):
            answer.append()
        '''
        