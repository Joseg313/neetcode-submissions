class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        hashmap = {}

        for i,num in enumerate(nums):
            #print(i, num)
            difference = target - num
            
            if difference in hashmap:
                answer.append(i)
                answer.append(hashmap[difference])
                return(sorted(answer))
            else:
                hashmap[num] = i
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
            for i in range(len(nums)):  
                for j in range(len(nums)-i-1):
                    if nums[i] + nums[j+1+i] == target:
                        answer.append(i)
                        answer.append(j+1+i)
                        return sorted(answer)
        '''
