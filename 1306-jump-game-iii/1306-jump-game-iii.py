from queue import Queue

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        ans = False
        n = len(arr)
        dp = [-1] * n

        q = []
        q.append(start)
        dp[start] = 0
        while q:
            cur_index = q.pop()
            
            if arr[cur_index] == 0:
                ans = True
                break
            
            next_plus = cur_index + arr[cur_index]
            next_minus = cur_index - arr[cur_index]

            if next_plus < n and dp[next_plus] == -1:
                dp[next_plus] = dp[cur_index] + 1
                q.append(next_plus)
            if next_minus >= 0 and dp[next_minus] == -1:
                dp[next_minus] = dp[cur_index] + 1
                q.append(next_minus)
            
        return ans
            