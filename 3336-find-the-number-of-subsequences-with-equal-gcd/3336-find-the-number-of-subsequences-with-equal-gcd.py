from functools import lru_cache
from math import gcd
from typing import List

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        @lru_cache(None)
        def dp(i: int, g1: int, g2: int) -> int:
            # 기저 조건: 모든 원소를 확인했을 때
            if i == n:
                # 두 부분 수열이 모두 비어있지 않고, GCD가 같아야 함
                if g1 != 0 and g2 != 0 and g1 == g2:
                    return 1
                return 0

            # 1. 현재 원소를 사용하지 않음
            res = dp(i + 1, g1, g2)
            
            # 2. 현재 원소를 seq1에 추가
            res += dp(i + 1, gcd(g1, nums[i]), g2)

            # 3. 현재 원소를 seq2에 추가
            res += dp(i + 1, g1, gcd(g2, nums[i]))

            return res % MOD

        return dp(0, 0, 0)