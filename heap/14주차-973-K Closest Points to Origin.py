class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for (x, y) in points:
            # Use negative distance to simulate max-heap
            distance = -(x**2 + y**2)
            if len(max_heap) < k:
                heapq.heappush(max_heap, (distance, (x, y)))
            else:
                heapq.heappushpop(max_heap, (distance, (x, y)))

        return [point for (distance, point) in max_heap]
