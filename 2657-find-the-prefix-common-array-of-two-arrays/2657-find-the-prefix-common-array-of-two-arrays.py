class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        d = dict()
        C = []
        n = len(A)

        for i in range(n):
            a, b = A[i], B[i]
            
            cnt = 0
            if a in d:
                d[a] += 1
                cnt += 1
            else:
                d[a] = 1
            
            if b in d:
                d[b] += 1
                cnt += 1
            else:
                d[b] = 1
            
            if i > 0:
                C.append(C[-1] + cnt)
            else:
                C.append(cnt)

        return C