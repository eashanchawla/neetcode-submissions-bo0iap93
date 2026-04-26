class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i: [] for i in range(n)}
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        from collections import deque
        visited = set()
        parts = 0
        for i in range(n):
            
            if i not in visited:
                q = deque()
                q.append(i)
                while q:
                    curr = q.popleft()
                    for neighbor in adjList[curr]:
                        if neighbor in visited:
                            continue
                        q.append(neighbor)
                        visited.add(neighbor)
                parts += 1
        return parts
                    

