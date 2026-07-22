class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # 연속 구간(run)으로 쪼개기
        runs = []  # (문자, 길이)
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            runs.append((s[i], j - i))
            i = j

        total_ones = sum(length for ch, length in runs if ch == '1')

        best_delta = 0
        # 0블록 - 1블록 - 0블록 패턴에서 두 0블록 합이 delta 후보
        for k in range(1, len(runs) - 1):
            if runs[k][0] == '1' and runs[k-1][0] == '0' and runs[k+1][0] == '0':
                best_delta = max(best_delta, runs[k-1][1] + runs[k+1][1])

        return total_ones + best_delta
