class Solution:
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def getPosibleMoves(self, point, m, n):
        x, y = point
        res = []
        for move in self.moves:
            dx, dy = move
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n:
                res.append((nx, ny))
        return res

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def dfs(start, visited):
            visited.add(start)
            ans = 0
            for nxt in self.getPosibleMoves(start, m, n):
                nx, ny = nxt
                if nxt not in visited and grid[ny][nx] != 0:
                    res = dfs(nxt, visited)
                    if res > ans:
                        ans = res
            # backtracking 시 이미 방문한 노드라도 다시 방문하는 경우의 수가 있음
            visited.remove(start)
            sx, sy = start
            return grid[sy][sx] + ans

        ans = 0
        for x in range(m):
            for y in range(n):
                if grid[y][x] != 0:
                    res = dfs((x, y), set())
                    if res > ans:
                        ans = res
        return ans