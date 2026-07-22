class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count('1')
        
        # 양 끝에 '1'이 있다고 가정
        prev_zero = 0   # 이전 0 블록의 길이
        cur_zero = 0    # 현재 0 블록의 길이
        best_gain = 0
        found_zero = False
        
        for ch in s:
            if ch == '0':
                cur_zero += 1
                found_zero = True
            else:  # ch == '1'
                if found_zero:
                    # 0 블록이 끝났을 때, 이전 0 블록과 현재 0 블록의 합 계산
                    if prev_zero > 0:
                        best_gain = max(best_gain, prev_zero + cur_zero)
                    prev_zero = cur_zero
                    cur_zero = 0
                    found_zero = False
        
        # 문자열 끝에 도달했을 때 마지막 0 블록 처리
        if found_zero and prev_zero > 0:
            best_gain = max(best_gain, prev_zero + cur_zero)
        
        return ones + best_gain