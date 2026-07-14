class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        dp = {(0, 0): 1}  # key: (g1, g2), value: 경우의 수

        for x in nums:
            new_dp = {}
            for (g1, g2), cnt in dp.items():
                # 1. Skip
                new_dp[(g1, g2)] = (new_dp.get((g1, g2), 0) + cnt) % MOD
                # 2. seq1에 추가
                ng1 = gcd(g1, x)
                new_dp[(ng1, g2)] = (new_dp.get((ng1, g2), 0) + cnt) % MOD
                # 3. seq2에 추가
                ng2 = gcd(g2, x)
                new_dp[(g1, ng2)] = (new_dp.get((g1, ng2), 0) + cnt) % MOD
            dp = new_dp

        answer = 0
        for (g1, g2), cnt in dp.items():
            if g1 != 0 and g1 == g2:
                answer = (answer + cnt) % MOD
        return answer