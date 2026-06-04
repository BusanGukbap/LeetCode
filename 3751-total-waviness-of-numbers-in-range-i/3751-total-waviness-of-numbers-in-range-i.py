import math

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total = 0
        for n in range(num1, num2 + 1):
            digits = str(n)
            for i in range(1, len(digits) - 1):
                d = int(digits[i])
                left = int(digits[i - 1])
                right = int(digits[i + 1])
                if d > left and d > right:
                    total += 1
                elif d < left and d < right:
                    total += 1
        return total