class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = []
        for num in nums:
            if not num in unique:
                unique.append(num)
            else:
                return True

        return False