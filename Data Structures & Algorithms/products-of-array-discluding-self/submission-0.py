class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # multiply all the numbers in the list together
        total_mult = 1
        zero = 0
        for num in nums:
            if num == 0:
                zero += 1
            else:
                total_mult = total_mult * num
        
        # divide the current index from total_mult 
        output = [] 
        if zero == 1: 
            for num in nums:
                if num != 0:
                    output.append(0)
                else:
                    output.append(total_mult)
        elif zero > 1:
            output = [0] * len(nums)
        else:
            for num in nums:
                output.append(int(total_mult / num))
            
        
        return output