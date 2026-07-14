class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        result = []

        # 잘라낼 길이를 2자리부터 9자리까지 늘려가며
        for length in range(2, len(digits) + 1):
            # 그 길이만큼 왼쪽부터 한 칸씩 밀며 잘라냄
            for start in range(len(digits) - length + 1):
                num = int(digits[start:start + length])
                if low <= num <= high:
                    result.append(num)

        return result
