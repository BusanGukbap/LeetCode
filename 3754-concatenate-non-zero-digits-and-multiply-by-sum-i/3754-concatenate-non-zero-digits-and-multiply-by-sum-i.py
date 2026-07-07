class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        temp = str(n)
        m = 0

        for a in temp:
            if a == '0':
                continue
            
            x *= 10
            x += int(a)
            m += int(a)
        
        return x * m