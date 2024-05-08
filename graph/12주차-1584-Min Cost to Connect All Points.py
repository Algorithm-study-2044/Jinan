import heapq as hq
from collections import defaultdict


class Solution:
    def get_dist(self, p1: (int, int), p2: (int, int)) -> int:
        return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

    def mst(self, graph, start):
        visited = set()
        min_heap = [(0, start)]
        t_weight = 0

        while min_heap:
            weight, v = hq.heappop(min_heap)

            if v in visited:
                continue

            visited.add(v)
            t_weight += weight

            for w, v in graph[v]:
                if v not in visited:
                    hq.heappush(min_heap, (w, v))

        return t_weight

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        G = defaultdict(set)
        for p1 in points:
            p1 = (p1[0], p1[1])
            for p2 in points:
                p2 = (p2[0], p2[1])
                G[p1].add((self.get_dist(p1, p2), p2))

        start = (points[0][0], points[0][1])
        return self.mst(G, start)
