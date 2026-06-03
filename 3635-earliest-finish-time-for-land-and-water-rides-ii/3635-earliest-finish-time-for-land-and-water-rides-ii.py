from bisect import bisect_right
from math import inf

class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration) -> int:
        def solve(start1, dur1, start2, dur2):
            rides2 = sorted(zip(start2, dur2))
            m = len(rides2)

            pref_min_dur = [0] * m
            pref_min_dur[0] = rides2[0][1]
            for i in range(1, m):
                pref_min_dur[i] = min(pref_min_dur[i - 1], rides2[i][1])

            suf_min_finish = [0] * m
            suf_min_finish[-1] = rides2[-1][0] + rides2[-1][1]
            for i in range(m - 2, -1, -1):
                suf_min_finish[i] = min(rides2[i][0] + rides2[i][1], suf_min_finish[i + 1])

            starts2 = [r[0] for r in rides2]

            ans = inf
            for s, d in zip(start1, dur1):
                f1 = s + d

                mid = bisect_right(starts2, f1) - 1

                if mid >= 0:
                    ans = min(ans, f1 + pref_min_dur[mid])

                if mid + 1 < m:
                    ans = min(ans, suf_min_finish[mid + 1])

            return ans

        return min(
            solve(landStartTime, landDuration, waterStartTime, waterDuration),
            solve(waterStartTime, waterDuration, landStartTime, landDuration),
        )