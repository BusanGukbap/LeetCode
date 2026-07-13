class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr2 = sorted(list(set(arr)))

        d = dict()
        for i, e in enumerate(arr2):
            if e not in d:
                d[e] = i+1
        
        ans = list()
        for a in arr:
            ans.append(d[a])
        
        return ans