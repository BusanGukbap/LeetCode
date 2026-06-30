class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0

        last = [-1]*3

        n = len(s)

        for i in range(n):
            pos = ord(s[i]) - ord('a')

            last[pos] = i

            ans += 1 + min(last)

        return ans