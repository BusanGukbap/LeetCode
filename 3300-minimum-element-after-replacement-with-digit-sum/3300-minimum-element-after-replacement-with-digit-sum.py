class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = 10**4

        for a in nums:
            temp = 0
            while a:
                temp += a%10
                a //= 10
            
            ans = min(ans, temp)
        
        return ans