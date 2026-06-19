class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        altitude = 0
        for a in gain:
            altitude += a
            ans = max(ans, altitude)
        return ans