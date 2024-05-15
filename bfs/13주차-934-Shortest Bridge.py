from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def get_neighbors(x, y):
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    yield nx, ny

        # Function to find one island and return its coordinates
        def bfs_find_island(start_x, start_y):
            queue = deque([(start_x, start_y)])
            island = set([(start_x, start_y)])
            grid[start_x][start_y] = -1  # Mark visited by flipping to -1
            while queue:
                x, y = queue.popleft()
                for nx, ny in get_neighbors(x, y):
                    if grid[nx][ny] == 1:
                        grid[nx][ny] = -1  # Mark as visited
                        island.add((nx, ny))
                        queue.append((nx, ny))
            return island

        # Find first island
        first_island = None
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    first_island = bfs_find_island(i, j)
                    break
            if first_island:
                break

        # BFS from the first island to reach the second island with the minimum number of flips
        queue = deque([(x, y, 0)
                      for x, y in first_island])  # include step count
        # Start with the first island already visited
        visited = set(first_island)

        while queue:
            x, y, step = queue.popleft()
            for nx, ny in get_neighbors(x, y):
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    if grid[nx][ny] == 0:
                        queue.append((nx, ny, step + 1))
                    elif grid[nx][ny] == 1:
                        return step  # Found the second island, return step count

        return -1  # If no connection is possible, which should not happen due to problem constraints
