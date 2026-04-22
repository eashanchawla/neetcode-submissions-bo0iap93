from collections import deque
class Solution:
    def bfs(self, grid, i, j):
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque([(i, j)])
        grid[i][j] =0
        islandsize = 0
        while q:
            i, j = q.popleft()
            islandsize += 1
            for x, y in neighbors:
                l, r = i + x, j + y
                if l < 0 or r < 0 or l >= len(grid) or r >= len(grid[0]) or grid[l][r] == 0:
                    continue
                grid[l][r] = 0
                q.append((l, r))
                
        return islandsize


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxIslandSize = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    islandSize = self.bfs(grid, i, j)
                    maxIslandSize = max(maxIslandSize, islandSize)
        return maxIslandSize
            