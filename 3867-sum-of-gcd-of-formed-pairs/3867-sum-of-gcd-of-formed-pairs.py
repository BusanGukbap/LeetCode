import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mx = list()
        prefixGcd = list()

        mx.append(nums[0])
        prefixGcd.append(math.gcd(nums[0], mx[0]))
        
        n = len(nums)

        for i in range(1, n):
            mx.append(max(mx[i-1], nums[i]))
            prefixGcd.append(math.gcd(nums[i], mx[i]))

        
        prefixGcd.sort()

        ans = 0

        for i in range(n//2):
            ans += math.gcd(prefixGcd[i], prefixGcd[n-i-1])
        
        return ans