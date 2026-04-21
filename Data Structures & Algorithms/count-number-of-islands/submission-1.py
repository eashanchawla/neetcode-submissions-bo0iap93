from collections import deque
class Solution:
    def bfs(self, grid: List[List[str]], i: int, j:int) -> List[List[str]]:
        queue = deque()
        queue.append((i, j))
        grid[i][j] = '0'
        neigbors = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while queue:
            curr_i, curr_j = queue.popleft()
            for n_x, n_y in neigbors:
                l, r = curr_i + n_x, curr_j + n_y
                if l < 0 or l >= len(grid) or r < 0 or r >= len(grid[0]) or grid[l][r] == '0':
                    continue
                queue.append((l, r))
                grid[l][r] = '0'
        return grid            

    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    # suspected island
                    grid = self.bfs(grid, i, j)
                    numIslands += 1
        return numIslands