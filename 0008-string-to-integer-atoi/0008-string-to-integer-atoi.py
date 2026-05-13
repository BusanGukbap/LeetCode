class Solution:
    def myAtoi(self, s: str) -> int:
        s = s[0:]
        ans = 0
        is_Positive = True
        is_start = False

        for i in range(len(s)):
            temp = s[i]
            if temp == ' ' and is_start == False:
                continue
            elif temp in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                ans *= 10
                ans += int(temp)
                is_start = True
            elif temp == '-' and is_start == False:
                is_Positive = False
                is_start = True
            elif temp == '+' and is_start == False:
                is_start = True
            else:
                break

        if not is_Positive:
            ans *= -1
        
        if ans < (-1)*(2**31):
            ans = (-1)*(2**31)
        if ans > 2**31-1:
            ans = 2**31-1

        return ans
