from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0

        graph = defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)

        q = deque([0])
        visited = {0}
        steps = 0

        while q:
            for _ in range(len(q)):
                index = q.popleft()
                if index == n-1:
                    return steps

                cur = arr[index]
                for neighbor in [index-1, index+1]:
                    if 0 <= neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
                for neighbor in graph[arr[index]]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
                
                del graph[arr[index]]
            steps += 1
        
        return -1