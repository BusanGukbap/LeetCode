class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans = float('inf')
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                end1 = landStartTime[i] + landDuration[i]
                end1 = max(end1, waterStartTime[j]) + waterDuration[j]

                end2 = waterStartTime[j] + waterDuration[j]
                end2 = max(end2, landStartTime[i]) + landDuration[i]
                ans = min(ans, end1, end2)
        return ans