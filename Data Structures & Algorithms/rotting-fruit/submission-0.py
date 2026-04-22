from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_count = 0
        rotten_list = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten_list.append((i, j))
                if grid[i][j] == 1:
                    fresh_count += 1

        q = deque(rotten_list)

        minutes = 0
        while q and fresh_count > 0:
            for _ in range(len(q)):
                i, j = q.popleft()

                for n_x, n_y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    l, r = i + n_x, j + n_y
                    if l < 0 or r < 0 or l >= len(grid) or r >= len(grid[0]) or grid[l][r] != 1:
                        continue
                    fresh_count -= 1
                    grid[l][r] = 2
                    q.append((l, r))
            
            minutes += 1
        
        if fresh_count > 0:
            return -1
        else:
            return minutes
