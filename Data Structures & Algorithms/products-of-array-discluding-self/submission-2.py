class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        # forward pass
        for i in range(1, len(nums)):
            output[i] = output[i-1]*nums[i-1]

        # backward pass
        end = 1
        for i in range(len(nums)-2, -1, -1):
            end = end * nums[i+1]
            output[i] = output[i]*end
        
        
        
        return output