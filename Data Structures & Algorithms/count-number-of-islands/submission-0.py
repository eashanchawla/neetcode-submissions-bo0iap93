class Solution:
    def find_neighbors(self, x_lim, y_lim, x, y):
        poss_neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        neighbors = []
        for poss_x, poss_y in poss_neighbors:
            if x + poss_x >= 0 and x + poss_x < x_lim and y + poss_y >= 0 and y + poss_y < y_lim:
                neighbors.append((x + poss_x, y + poss_y))
        return neighbors 

    def bfs(self, row, col, grid):
        q = [(row, col)]
        grid[row][col] = '0'

        while q:
            current_row, current_col = q.pop(0)
            neigs = self.find_neighbors(len(grid), len(grid[0]), current_row, current_col)
            for neighbor_x, neighbor_y in neigs:
                if grid[neighbor_x][neighbor_y] == '1':
                    grid[neighbor_x][neighbor_y] = '0'
                    q.append([neighbor_x, neighbor_y])

    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    num_islands += 1
                    self.bfs(i, j, grid)
        return num_islands