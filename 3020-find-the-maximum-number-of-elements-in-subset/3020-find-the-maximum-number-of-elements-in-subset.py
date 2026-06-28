class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        ans = 1
        
        d = dict()
        for a in nums:
            if a not in d:
                d[a] = 1
            else:
                d[a] += 1
        
        if 1 in d:
            c = d[1]
            if c % 2 == 1:
                ans = c
            else:
                ans = c - 1
        
        for x in d:
            if x == 1:
                continue
            
            cur = x
            length = 0
            while cur in d and d[cur] >= 2:
                length += 1
                cur = cur**2
            
            if cur in d:
                total = 2*length + 1
            else:
                total = 2 * (length - 1) + 1
            ans = max(ans, total)

        return ans
        