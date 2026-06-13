class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = ""
        for word in words:
            total = 0
            for a in word:
                temp = ord(a) - ord('a')
                # print(temp)
                total += weights[temp]
            
            total %= 26
            # print()
            ans += chr(ord('z') - total)
        
        return ans
