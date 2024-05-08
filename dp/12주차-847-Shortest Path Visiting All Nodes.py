class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        final_mask = (1 << n) - 1
        queue = deque([(i, 1 << i, 0) for i in range(n)])
        visited = {(i, 1 << i) for i in range(n)}

        while queue:
            node, mask, dist = queue.popleft()

            if mask == final_mask:
                return dist

            for neighbor in graph[node]:
                next_mask = mask | (1 << neighbor)
                if (neighbor, next_mask) not in visited:
                    visited.add((neighbor, next_mask))
                    queue.append((neighbor, next_mask, dist + 1))

        return -1
