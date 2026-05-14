class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        m = max(nums)
        
        
        if n - 1 != m:
            return False
        
        nums.sort()

        for i in range(n-1):
            if nums[i] != i+1:
                return False

        if nums[-1] != m:
            return False
        
        return True