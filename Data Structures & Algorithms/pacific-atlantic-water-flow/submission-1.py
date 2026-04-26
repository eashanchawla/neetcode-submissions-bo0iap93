from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac_start, at_start = [], []
        for i in range(len(heights)):
            pac_start.append((i, 0))
            at_start.append((i, len(heights[0]) - 1))
        for i in range(1, len(heights[0])):
            pac_start.append((0, i))
        for i in range(0, len(heights[0])):
            at_start.append((len(heights) - 1, i))
        pac_set = set(pac_start)
        atl_set = set(at_start)
        q = deque(pac_start)

        neighbors = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while q:
            x, y = q.popleft()
            for nx, ny in neighbors:
                l, r = x + nx, y + ny
                if l < 0 or r < 0 or l >= len(heights) or r >= len(heights[0]) or heights[l][r] < heights[x][y] or (l, r) in pac_set:
                    continue
                q.append((l, r))
                pac_set.add((l, r))

        q_at = deque(at_start)
        while q_at:
            x, y = q_at.popleft()
            for nx, ny in neighbors:
                l, r = x + nx, y + ny
                if l < 0 or r < 0 or l >= len(heights) or r >= len(heights[0]) or heights[l][r] < heights[x][y] or (l, r) in atl_set:
                    continue
                q_at.append((l, r))
                atl_set.add((l, r))
        
        return list(pac_set & atl_set)
            
    