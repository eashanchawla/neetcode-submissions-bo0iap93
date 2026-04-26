from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac_set, atl_set = set(), set()
        for i in range(len(heights)):
            pac_set.add((i, 0))
            atl_set.add((i, len(heights[0]) - 1))
        for i in range(1, len(heights[0])):
            pac_set.add((0, i))
        for i in range(0, len(heights[0])):
            atl_set.add((len(heights) - 1, i))
        
        q = deque(pac_set)
        q_at = deque(atl_set)

        neighbors = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while q:
            x, y = q.popleft()
            for nx, ny in neighbors:
                l, r = x + nx, y + ny
                if l < 0 or r < 0 or l >= len(heights) or r >= len(heights[0]) or heights[l][r] < heights[x][y] or (l, r) in pac_set:
                    continue
                q.append((l, r))
                pac_set.add((l, r))

        
        while q_at:
            x, y = q_at.popleft()
            for nx, ny in neighbors:
                l, r = x + nx, y + ny
                if l < 0 or r < 0 or l >= len(heights) or r >= len(heights[0]) or heights[l][r] < heights[x][y] or (l, r) in atl_set:
                    continue
                q_at.append((l, r))
                atl_set.add((l, r))
        
        return list(pac_set & atl_set)
            
    