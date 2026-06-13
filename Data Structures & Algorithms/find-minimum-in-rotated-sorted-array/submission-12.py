class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums)-1
        m = int(r/2)
        # print(l,m,r)
        while len(nums) > 0:
            print(l,m,r)
            # minimum has been gound
            if l == m and m == r:
                return nums[l]
            # right side has the correct answer
            elif nums[l] <= nums[m] and nums[r] <= nums[m]:
                # keep m+1 to r, drop rest
                nums = nums[m+1:]
                # update l,r,m
                l = 0
                r = len(nums)-1
                m = int(r/2)
            # left side has the correct answer
            elif nums[l]<=nums[m] and nums[r]>=nums[m]:
                nums = nums[0:m+1]
                l=0
                r = len(nums)-1
                m = int(r/2)
            # mid has the correct answer
            elif nums[l]>=nums[m] and nums[r]>=nums[m]:
                nums=nums[l:m+1]
                l = 0
                r = len(nums)-1
                m = int(r/2)

