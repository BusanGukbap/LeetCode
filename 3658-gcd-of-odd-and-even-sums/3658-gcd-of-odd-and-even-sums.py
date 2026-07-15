import math

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = 0
        sumEven = 0

        for i in range(n):
            sumOdd += 1 + i*2
            sumEven += 2 + i*2
        
        return math.gcd(sumOdd, sumEven)