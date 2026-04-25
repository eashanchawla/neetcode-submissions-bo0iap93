from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        while q:
            curr_x, curr_y = q.popleft()
            nes = [(0,1), (1,0), (-1,0),(0,-1)]
            for nx, ny in nes:
                l, r = curr_x + nx, curr_y + ny
                if l < 0 or r < 0 or l >= len(grid) or r >= len(grid[0]) or grid[l][r] != INF:
                    continue
                
                grid[l][r] = grid[curr_x][curr_y] + 1
                q.append((l, r))
